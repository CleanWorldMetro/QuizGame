from back_end.config import dbconfig


connection = dbconfig.connection
def get_players():
    sql = "select * from player"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    players = get_players()
    print(players)