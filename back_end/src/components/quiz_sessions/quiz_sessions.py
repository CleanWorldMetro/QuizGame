import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
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




if __name__ == "__main__":
    # quiz_sessions = get_all_quiz_sessions()
    # all_closed_quiz_sessions = get_all_closed_quiz_sessions()
    all_openned_quiz_sessions = get_all_openned_quiz_sessions()
    # print(quiz_sessions)
    # print(all_closed_quiz_sessions)
    print(all_openned_quiz_sessions)

    class Quiz_session:
        def __init__(self,player_id,questions_answered,correct_count,chances,is_open):
            self.play_id = player_id
            self.questions_answered = questions_answered
            self.correct_count = correct_count
            self.chances = chances
            self.is_open = is_open
        # quiz_session = Quiz_session(player_id,questions_answered,correct_count,chances,is_open)