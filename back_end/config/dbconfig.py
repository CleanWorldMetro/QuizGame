import mysql.connector

#db connection

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3300,
    database = "quiz",
    user = "root",
    password = "",
    autocommit = True
)

#openweather key:
private_key = "28e489100830be62a52cd6f528c12b6c"