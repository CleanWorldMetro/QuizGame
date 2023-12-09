import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from src.config import dbconfig

connection = dbconfig.connection

def get_all_current_quiz_sessions():
    sql = "select * from current_quiz_session"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_all_current_quiz_sessions_by_player(player_id):
    sql = "select * from current_quiz_session"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    final_sql = f"{sql} WHERE player_id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    # quiz_sessions = get_all_quiz_sessions()
    # all_closed_quiz_sessions = get_all_closed_quiz_sessions()
    player_id = 1
    all_current_quiz_sessions = get_all_current_quiz_sessions()
    all_current_quiz_sessions_by_player = get_all_current_quiz_sessions_by_player(player_id)
    # print(quiz_sessions)
    # print(all_closed_quiz_sessions)
    # print(all_current_quiz_sessions)
    # print(all_current_quiz_sessions)
    print(all_current_quiz_sessions_by_player)