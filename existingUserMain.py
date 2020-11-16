import sqlite3

def searchUser(username, password):
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    items = cursor.fetchall()

    for item in items:
        if item[0] == username and item[1] == password:
            return True

    connection.commit()
    connection.close()
