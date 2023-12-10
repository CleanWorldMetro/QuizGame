import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig

from src.components.location import cities,countries
from src.components.questions import questions,question_options
from src.components.players import players
from src.components.quiz_sessions import quiz_sessions, current_quiz_sessions

#when such username not exist, add that username to player table and add a new quiz_session with that new username to quiz_session table
def get_session_when_player_not_exist(username):
    players.insert_new_player(username)
    new_player = players.get_player_by_name(username) #[(3, 'hoa')]
    # print(new_player)
    quiz_sessions.insert_new_quiz_session(new_player[0][0])
    new_quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(new_player[0][0])
    print("when player not exist, creating new quiz session")
    return new_quiz_session
  
def get_session_when_player_exist(username):
  
    username_data = players.get_player_by_name(username)
    quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(username_data[0][0])
    
    # name is exist but no open quiz_session with that name
    if not quiz_session: 
      quiz_sessions.insert_new_quiz_session(username_data[0][0])
      new_opened_quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(username_data[0][0])
      quiz_session = new_opened_quiz_session
      print("when player exist but quiz_session closed, create new open quiz_session ")
    
    else:
      print("player exist and quiz_session open, getting that quiz_session")
    
    return quiz_session


def get_quiz_session_by_player_name(username):
  username_data = players.get_player_by_name(username)
  quiz_session = None
  # print(username_data)
  if not players.is_name_exist(username_data):
    quiz_session = get_session_when_player_not_exist(username)
  else:
    quiz_session = get_session_when_player_exist(username)
      
  return quiz_session

def do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player):
  print(f'quiz_session: {quiz_session_by_player}')
  print(f'answer by player: {answer_by_player}')
  session_id =  quiz_session_by_player[0][0]
  player_id= quiz_session_by_player[0][1]
  question_id  = answer_by_player[0][1]
  question_option_id = answer_by_player[0][0]
  is_correct = answer_by_player[0][3]
  current_quiz_sessions.insert_new_current_quiz_session(session_id,player_id,question_id,question_option_id,is_correct)  
  return

def quiz_session_when_answer_correct(quiz_session_by_player, answer_by_player):

  do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player)
  # session_id =  quiz_session_by_player
  # player_id=
  # question_id
  # question_option_id=
  # is_correct = 
  return

def quiz_session_when_answer_wrong(quiz_session_by_player, answer_by_player):
  do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player)

  
  return

def save_option_by_option_id(option_id, quiz_session_by_player):
  answer_option_data = question_options.get_option_by_option_id(option_id)
  # question_id = 
  is_correct = question_options.option_is_correct(answer_option_data)

  print(f'answer is correct: {is_correct}')
  if is_correct:
    new_quiz_session = quiz_session_when_answer_correct(quiz_session_by_player,answer_option_data)
  else:
    new_quiz_session = quiz_session_when_answer_wrong(quiz_session_by_player,answer_option_data)
  return

def game() :
  username = 'hoa'
  quiz_session = get_quiz_session_by_player_name(username)
  # answer_option_id = request.form.get("option_id")
  # print(quiz_session)
  answer_option_id = 19
  save_option_by_option_id(answer_option_id,quiz_session)


if __name__ == "__main__":
  game()