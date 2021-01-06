# Import all necessary packages
import sqlite3  # Import sqlite for database
import main_def_func  # Define all the functions used here
import password_keeper  # Goes to another section where all the passwords are kept (encrypted)
import password_keeper_def_func  # Defines all functions for the password_keeper
import cryptographyDefFunc  # Defines all the functions for encrypting, decrypting getting and setting the keys, etc.
from tkinter import *  # Used for the graphical user interface (gui)
from tkinter import messagebox
import os

# Create main root window and configuring it
root = Tk()
root.title("Login / Signup")
root.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
width = 500
height = 300
root.geometry(str(width) + "x" + str(height))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (width/2))
y_coordinate = int((screen_height/2) - (height/2))
root.geometry(str(width) + "x" + str(height) + "+" + str(x_coordinate) + "+" + str(y_coordinate))

# Create Labels and Adjust them in main window
welcome_label = Label(root, text="Welcome!", font=("Times New Roman", 30))
welcome_label.grid(row=1, column=3, columnspan=100, padx=10, pady=10)
username_label = Label(root, text="Username:", font=("Times New Roman", 15))
username_label.grid(row=5, column=3, padx=3, pady=10)
password_label = Label(root, text="Password:", font=("Times New Roman", 15))
password_label.grid(row=7, column=3, padx=3, pady=10)

# Create Entry and Adjust them in main window
username_entry = Entry(root, width=50)
username_entry.grid(row=5, column=5, columnspan=2)
password_entry = Entry(root, width=50)
password_entry.grid(row=7, column=5, columnspan=2)

# Commands for buttons
def login():
    if (username_entry.get() == "" or password_entry.get() == ""):
        messagebox.showwarning("Warning", "The username or password fields are blank!")
    else:
        username = username_entry.get()  # gets username
        password = password_entry.get()  # gets password
        try:
            key = cryptographyDefFunc.get_key(username)  # Gets the key for the specified user
            # Because the username and password where encrypted when inserting into table we need to compare them
            if main_def_func.searchUser(key, username, password) == True:
                root.destroy()
                password_keeper.mainPasswordKeeper(username)  # We give all the necessary parameters
            else:
                messagebox.showerror("Error", "User has not been found. Please try again, or create an account.")
        except Exception as error:
            messagebox.showerror("Error", error)

def signup():
    if (username_entry.get() == "" or password_entry.get() == ""):
        messagebox.showwarning("Warning", "The username or password fields are blank!")
    else:
        try:
            main_def_func.tableCreate()  # Searches to see if database has all ready been created
        except sqlite3.OperationalError as error:
            messagebox.showwarning("Error", error)
        username = username_entry.get()  # gets username
        password = password_entry.get()  # gets password
        try:
            cryptographyDefFunc.set_key(username)  # sets key for encryption for specified user
            encrypted_user = cryptographyDefFunc.encrypt_some(username, password)  # encrypts user and password
            encrypted_username = encrypted_user[0]
            encrypted_password = encrypted_user[1]
            main_def_func.signup(encrypted_username,
                                 encrypted_password)  # creates record in first table with encrypted data
            password_keeper_def_func.createTable(username)  # Creates second table for that specified user
            root.destroy()
            password_keeper.mainPasswordKeeper(username)  # We give all the necessary parameters
        except Exception as error:
            messagebox.showwarning("Error", error)

def info():
    os.system('notepad ExtraSupportContent/about.txt')

# Create Buttons and Adjust them in main window
login_button = Button(root, text="Log In", font=("Times New Roman", 13), command=login)
login_button.grid(row=20, column=4, pady=15)
signup_button = Button(root, text="Sign Up", font=("Times New Roman", 13), command=signup)
signup_button.grid(row=20, column=6, pady=15)
info_button = Button(root, text="Info", font=("Times New Roman", 13), command=info)
info_button.grid(row=1000, column=5, padx=15, pady=15)

root.mainloop()

