
# import sys

from config import dbconfig
# from ...config import dbconfig

connection = dbconfig.connection

def get_countries():
    sql = "select * from country"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    print(sys.path)
    # countries = get_countries()
    # print(countries)