import sqlite3

def serchUser():
    validate = False

    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    items = cursor.fetchall()
    for item in items:
        if item[0] == username and item[1] == password:
            validate = True
        else:
            validate = False
    connection.commit()
    connection.close()

    if validate == True:
        return True
    else:
        return False
