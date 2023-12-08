# import sys
import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')

# sys.path.insert(1,'G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
#use 1 instead of 0 as 0 is reserved placed, not recommended to use 0

from config import dbconfig
# from ...config import dbconfig
# from ...config import dbconfig

connection = dbconfig.connection

def get_cities():
    sql = "select * from city"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    cities = get_cities()
    print(cities)



# G:/Metropolia/Metropolia/2023/Syksy/SOFTWARE_2/PROJECT/Quiz_Project/back_end/src