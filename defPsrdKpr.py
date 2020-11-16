import sqlite3

# Query the DB and returning ALL records
def show_all(username):
    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT rowid, * FROM " + username)
    items = c.fetchall()

    # Show results
    for item in items:
        print(item)

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
def name_lookup(username, name):
    # Connect to database
    conn = sqlite3.connect("registryUsers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM " + username + " WHERE username LIKE '" + name + "' ")
    items = c.fetchall()

    # Show results
    for item in items:
        print(item)

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
