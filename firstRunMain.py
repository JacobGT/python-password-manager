import sqlite3

def tableCreate():
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE users (
                    username text,
                    password text
                    )""")
    connection.commit()
    connection.close()
