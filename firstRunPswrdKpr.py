import sqlite3

def createTable(username):
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE " + username + "(username text, password text, email text, info text)")
    connection.commit()
    connection.close()