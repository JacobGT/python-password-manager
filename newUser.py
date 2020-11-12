import sqlite3

def signup():
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    info = (username, password)
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (
                        username,
                        password) 
                        VALUES(?,?)""", info)
    connection.commit()
    connection.close()
