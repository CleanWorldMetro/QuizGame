import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig

connection = dbconfig.connection

# class quiz
# class option

def get_all_quiz_sessions():
    sql = "select * from quiz_session"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_all_closed_quiz_sessions():
    sql = "select * from quiz_session"
    final_sql = f"{sql} WHERE is_open = 0"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result

def get_all_openned_quiz_sessions():
    sql = "select * from quiz_session"
    final_sql = f"{sql} WHERE is_open = 1"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result

def get_open_quiz_session_by_player_id(player_id):
    
    sql = "select * from quiz_session"
    final_sql = f"{sql} WHERE is_open = 1 and player_id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    
    return result

def insert_new_quiz_session(player_id):
    tables ="player_id,questions_answered,correct_counts,chances,is_open"
    values = f"{player_id},0,0,3,1"
    sql = "INSERT INTO quiz_session"
    more_sql = f"{sql} ({tables})"
    final_sql=f"{more_sql} VALUES ({values})"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    # result = cursor.fetchall()
    print("Insert new quiz session successfully")

    return 


if __name__ == "__main__":
    # quiz_sessions = get_all_quiz_sessions()
    # all_closed_quiz_sessions = get_all_closed_quiz_sessions()
    quiz_session1 = get_open_quiz_session_by_player_id(1)
    # print(quiz_sessions)
    # print(all_closed_quiz_sessions)
    print(insert_new_quiz_session(2))

    # class Quiz_session:
    #     def __init__(self,player_id,questions_answered,correct_count,chances,is_open):
    #         self.play_id = player_id
    #         self.questions_answered = questions_answered
    #         self.correct_count = correct_count
    #         self.chances = chances
    #         self.is_open = is_open
        # quiz_session = Quiz_session(player_id,questions_answered,correct_count,chances,is_open)