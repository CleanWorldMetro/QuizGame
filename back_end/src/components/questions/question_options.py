import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from config import dbconfig
connection = dbconfig.connection

def get_all_options():
    sql = "select * from quiz_question_option"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    options = get_all_options()
    print(options)
