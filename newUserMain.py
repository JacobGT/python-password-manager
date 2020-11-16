import sqlite3

def signup(username, password):

    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?)", (username, password))
    connection.commit()
    connection.close()
