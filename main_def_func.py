import sqlite3
from cryptography.fernet import Fernet

def signup(username, password):
    # Inserts username and password to database (both are encrypted)
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?)", (username, password))
    connection.commit()
    connection.close()


def searchUser(key, username, password):
    # Compares if the user and password are correct and if the account exists

    # Gets a hold of the key of the specified user to decrypt the info
    f = Fernet(key)

    # Connect to database
    conn = sqlite3.connect("registryUsers.db")
    # Create a cursor
    c = conn.cursor()
    # Query database
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    for item in items:
        # Decrypts the username of the user
        decrypted_user = f.decrypt(item[0])
        # Decode the encoded user
        original_user = decrypted_user.decode()

        # Decrypts the password of the user
        decrypted_pass = f.decrypt(item[1])
        # Decode the encoded pass
        original_pass = decrypted_pass.decode()
        if original_user == username and original_pass == password:
            return True

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def tableCreate():
    # Creates database table
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE users (
                    username text,
                    password text
                    )""")
    connection.commit()
    connection.close()
