from back_end.config import dbconfig

connection = dbconfig.connection

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