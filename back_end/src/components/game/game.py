import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend')

from back_end.src.components.location import cities,countries
from components.questions import questions,question_options
from components.players import players


def get_quiz_session_by_player(username):
  username_data = players.get_player_by_name(username)
  quiz_session = None
  print(username_data)
  if not players.is_name_exist(username_data):
    return
      
      
  return quiz_session

if __name__ == "__main__":
  username = input("type username")
  game(username)