from flask import Flask, redirect, render_template, request, url_for, session
from src.components.location import cities,countries
from src.components.questions import questions,question_options
from src.components.players import players

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
    return render_template("index.html", quiz_session = quiz_session)
  
@app.route("/login", methods = ["POST","GET"])
def login():
  
  if "quiz_session" in session:
    return redirect(url_for("index"))
  
  if request.method == "POST":
    username = request.form.get("username")
    username_data = players.get_player_by_name(username)
    if not players.is_name_exist(username_data):
    
    #set quiz_session to session  
    #return quiz_session
      
      return redirect(url_for("index"))
    
  
  return render_template("login.html")
    
    

@app.route("/worldmap")
def worldmap():
  if request.method == "GET":
    country_list = countries.get_countries()
    location_list = cities.get_cities()
    # print(country_list.size)
    return render_template("worldmap.html", country_list = country_list, location_list = location_list)
  else:
    location_id = request.form.get("location_id")
    location_in_request = cities.get_city_by_id(location_id)
    # print(location_in_request)
    return redirect(url_for("location",city_name = location_in_request[0][1].lower()))

@app.route("/location/<city_name>", methods = ["POST","GET"])
def location(city_name):
  if request.method == "GET":
    city_in_request = cities.get_city_by_name(city_name)
    question = questions.get_random_question_by_location_id(city_in_request[0][0])
    options_of_question = question_options.get_options_by_question_id(question[0][0])
    print(options_of_question)
    
    return render_template("question.html",city_in_request=city_in_request,question=question,options_of_question=options_of_question)
  else:
    answer_question_option_id = request.form.get("option_id")
    answer_option = question_options.get_option_by_option_id(answer_question_option_id)
    question_id = answer_option[0][1]
    is_correct = answer_option[0][3]
    #log the answer from user as new current session
    #up session belong to this user
    
    return "hi"

@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("index"))  



if __name__ == "__main__":
  app.run(debug=True)

