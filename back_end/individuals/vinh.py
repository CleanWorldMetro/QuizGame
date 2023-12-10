

# def main():
# # implement login function as a OOP

#  implemet login function
#  user type username
#
#  using databse to check that username
#  yes: fetch the session with that name
#  no: create a session with that name
#
#  user = input("type user")
#  check_user(user) #return session associating with this user
#  if user in database
#    quiz_session_by_user = fetch session_by_user
#  else:
#    create new_session_by_user
#    quiz_session_by_user = new_session_by_user
#  return quiz_session_by_user
#
#  session_data = check_user(user)
#
#  convert this function into OOP
#  quiz_session = Quiz_session(session_data[0],session_data[1],session_data[3]],etc)
#
# if __name__ == "__main__":
#     main()
import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from src.config import dbconfig
connection = dbconfig.connection
def fetch_user(user):
    sql="select player.name from player"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"the name of airport {row[0]}")
    return

