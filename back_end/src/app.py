from flask import Flask, redirect, render_template, request, url_for, session, flash
from src.components.location import cities,countries
from src.components.questions import questions,question_options
from src.components.players import players
from src.components.game import game
from src.components.quiz_sessions import quiz_sessions, current_quiz_sessions

from flask_session import Session

app = Flask( __name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/index")
@app.route("/home")
@app.route("/", methods = ["POST","GET"])
def index():
  
  quiz_session = session.get("quiz_session")
  
  if not quiz_session:
    return redirect(url_for("login"))
  else:
    correct_counts = quiz_session[3]
    chances = quiz_session[4]
    if correct_counts >= 10 or chances <= 0:
      return redirect(url_for("finish"))
    return render_template("index.html", quiz_session = quiz_session)
  
@app.route("/login", methods = ["POST","GET"])
def login():
  
  if "quiz_session" in session:
    return redirect(url_for("index"))
  
  if request.method == "POST":
    username = request.form.get("username")
    quiz_session = game.get_quiz_session_by_player_name(username)
    session["quiz_session"] = quiz_session[0]
    flash('Welcome to the Quiz World')
    return redirect(url_for("index"))
    
  return render_template("login.html")
    
    

@app.route("/worldmap", methods = ["POST","GET"])
def worldmap():
  quiz_session = session["quiz_session"]
  if request.method == "GET":
    country_list = countries.get_countries()
    location_list = cities.get_cities()
    
    correct_points = session["quiz_session"][3]
    chances = session["quiz_session"][4]
    #when victory or game_over
    if correct_points == 10 or chances == 0:
      return redirect(url_for("finish"))
    # print(country_list.size)
    return render_template("worldmap.html", country_list = country_list, location_list = location_list, quiz_session=quiz_session)
  else:
    location_id = request.form.get("location_id")
    location_in_request = cities.get_city_by_id(location_id)
    # print(location_in_request)
    return redirect(url_for("location",city_name = location_in_request[0][1].lower()))

@app.route("/location/<city_name>", methods = ["POST","GET"])
def location(city_name):
  quiz_session = session["quiz_session"]
  if request.method == "GET":
    city_in_request = cities.get_city_by_name(city_name)
    question = questions.get_random_question_by_location_id(city_in_request[0][0])
    options_of_question = question_options.get_options_by_question_id(question[0][0])
    # print(options_of_question)
    
    return render_template("question.html",city_in_request=city_in_request,question=question,options_of_question=options_of_question,quiz_session = quiz_session)
  else:
    answer_question_option_id = request.form.get("option_id")
    quiz_session_by_player = session['quiz_session']
    # print(answer_question_option_id) # 12
    # print(f"current quiz session: {quiz_session_by_player}") # (3, 3, 0, 0, 3, 1)
    updated_quiz_session = game.save_option_by_option_id(answer_question_option_id,quiz_session_by_player)[0]

    #update quiz_session
    session["quiz_session"] = updated_quiz_session
    

    # print(updated_quiz_session)
    # answer_option = question_options.get_option_by_option_id(answer_question_option_id)
    # question_id = answer_option[0][1]
    # is_correct = answer_option[0][3]
    #log the answer from user as new current session
    #up session belong to this user
    return redirect(url_for("worldmap"))
  
@app.route("/finish", methods = ["POST","GET"])
def finish():
  quiz_session = session['quiz_session']
  print(quiz_session)
  if request.method == "GET":
    correct_counts = quiz_session[3]
    chances = quiz_session[4]
    return  render_template("finish.html",quiz_session = quiz_session, correct_counts = correct_counts, chances = chances )
  else:
    quiz_session_id = quiz_session[0]
    player_id =  quiz_session[1]
    print(f'quiz_session_id: {quiz_session_id}')
    print(f'player id: {player_id}')
    quiz_sessions.update_quiz_session_when_finish(quiz_session_id)
    quiz_sessions.insert_new_quiz_session(player_id)
    new_quiz_session_by_same_player_id = quiz_sessions.get_open_quiz_session_by_player_id(player_id)
    # print(f"this is a new quiz session: {new_quiz_session_by_same_player_id}")
    session['quiz_session'] = new_quiz_session_by_same_player_id[0]
    return redirect(url_for("worldmap"))
    

@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("index"))  



if __name__ == "__main__":
  app.run(debug=True)

