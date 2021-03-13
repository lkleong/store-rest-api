import sqlite3

connection = sqlite3.connect('data.db')
cusor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cusor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cusor.execute(create_table)

connection.commit()
connection.close()


