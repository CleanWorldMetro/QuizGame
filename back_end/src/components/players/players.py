import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend')
from src.config import dbconfig


connection = dbconfig.connection

def convert_name(name):
    return name.lower()

def is_name_exist(name_data):
    if len(name_data) != 0:
        return True
    else:
        return False


def get_players():
    sql = "select * from player"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_player_by_name(name):
    
    sql = "SELECT * from player"
    final_sql = sql + f" WHERE name = '{name}'"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result
    # return final_sql

if __name__ == "__main__":
    players = get_players()
    name1_data = get_player_by_name("hoa")
    print(name1_data)
    print(is_name_exist(name1_data))