import sqlite3
from cryptography.fernet import Fernet

# Query the DB and returning ALL records
def show_all(key, username):
    # Get key
    f = Fernet(key)

    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT rowid, * FROM " + username)
    items = c.fetchall()

    # Show results
    for item in items:
        # Decrypt and decode info
        decrypted_user = f.decrypt(item[1])
        original_user = decrypted_user.decode()

        decrypted_pass = f.decrypt(item[2])
        original_pass = decrypted_pass.decode()

        decrypted_email = f.decrypt(item[3])
        original_email = decrypted_email.decode()

        decrypted_info = f.decrypt(item[4])
        original_info = decrypted_info.decode()

        # Format results
        print("Id: " + str(item[0]))
        print("User/Website: " + original_user)
        print("Password: " + original_pass)
        print("Email: " + original_email)
        print("Info: " + original_info)
        print("-------------------------------------------------")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Add ONE new record to the table
def add_one(username, user, password, email, info):
    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("INSERT INTO " + username + " VALUES (?, ?, ?, ?)", (user, password, email, info))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Delete record from table
def delete_one(username, id):
    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("DELETE from " + username + " WHERE ROWID = (?)", id)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Lookup with WHERE
def name_lookup(key, username, name):
    # Get key
    f = Fernet(key)

    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT rowid, * FROM " + username)
    items = c.fetchall()

    # Searches through all items
    for item in items:
        # Decrypts the name of the record
        decrypted_name = f.decrypt(item[1])  # The rowid is in the '0' position, so name is in '1'
        original_name = decrypted_name.decode()

        # Compares the record to what the user entered
        if original_name == name:
            decrypted_pass = f.decrypt(item[2])
            original_pass = decrypted_pass.decode()

            decrypted_email = f.decrypt(item[3])
            original_email = decrypted_email.decode()

            decrypted_info = f.decrypt(item[4])
            original_info = decrypted_info.decode()

            # Format results
            print("Id: " + str(item[0]))
            print("User/Website: " + original_name)
            print("Password: " + original_pass)
            print("Email: " + original_email)
            print("Info: " + original_info)
            print("-------------------------------------------------")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Update record
def update_one(username, user, password, email, info, id):
    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    c.execute(" UPDATE " + username + " SET username = (?) WHERE rowid = (?)", (user, id))
    c.execute(" UPDATE " + username + " SET password = (?) WHERE rowid = (?)", (password, id))
    c.execute(" UPDATE " + username + " SET email = (?) WHERE rowid = (?)", (email, id))
    c.execute(" UPDATE " + username + " SET info = (?) WHERE rowid = (?)", (info, id))


    # Commit changes to db
    conn.commit()

    # Close connection to db
    conn.close()

# Creates table for specific user
def createTable(username):
    connection = sqlite3.connect("registryUsers.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE " + username + "(username text, password text, email text, info text)")
    connection.commit()
    connection.close()
