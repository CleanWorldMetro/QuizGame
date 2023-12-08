import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from config import dbconfig
# from 
connection = dbconfig.connection

def get_questions():
    sql = "select * from quiz_question"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# converting data to Ojbect

# object = {
#     "id": data[0]
#      question_name:data[1]
#     location:[2]
# }


if __name__ == "__main__":
    questions = get_questions()
    
    print(questions)

