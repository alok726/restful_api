import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

query = "INSERT INTO users VALUES(NULL, ?, ?)"

cursor.execute(query, ('Papun', 'password'))

connection.commit()
connection.close()