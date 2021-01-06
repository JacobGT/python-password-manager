import password_keeper_def_func  # Defines all the functions used in password_keeper
import cryptographyDefFunc  # Defines all the functions for encrypting, decrypting getting and setting the keys, etc.
import sqlite3  # Import sqlite for database
from tkinter import *  # Used for the graphical user interface (gui)
from tkinter import messagebox
from PIL import ImageTk, Image
import os

def mainPasswordKeeper(username):
    root = Tk()
    root.title("Welcome! - Password Manager")
    root.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
    width = 500
    height = 300
    root.geometry(str(width) + "x" + str(height))
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    root.geometry(str(width) + "x" + str(height) + "+" + str(x_coordinate) + "+" + str(y_coordinate))

    # Create Labels
    welcome_label = Label(root, text="Welcome, " + username + ".", font=("Times New Roman", 30))
    welcome_label.grid(row=1, column=1, columnspan=50, padx=10, pady=10)

    # Define Functions for buttons
    def view():
        try:
            # Gets the key for the specified user
            key = cryptographyDefFunc.get_key(username)
            # Shows all passwords, usernames, emails and info + rowid

            root.destroy()
            password_keeper_def_func.show_all(key, username)

        except Exception as error:
            messagebox.showerror("Error", error)
            print(error)

    def add():
        try:
            # Sees if table has all ready been created
            password_keeper_def_func.createTable(username)
        except sqlite3.OperationalError as error:
            pass
            # messagebox.showerror("Error", error)

        try:
            root.withdraw()
            add_new = Tk()
            add_new.title("Add Password")
            add_new.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
            width2 = 500
            height2 = 600
            add_new.geometry(str(width2) + "x" + str(height2))
            x_coordinate2 = int((screen_width / 2) - (width2 / 2))
            y_coordinate2 = int((screen_height / 2) - (height2 / 2))
            add_new.geometry(str(width2) + "x" + str(height2) + "+" + str(x_coordinate2) + "+" + str(y_coordinate2))

            # Create Labels
            info1_label = Label(add_new, text="What will be in the user field? (You can add the name of the website or the username, etc.)")
            info1_label.grid(row=0, column=0, pady=10)
            user_label = Label(add_new, text="Username/Website URL:", font=("Times New Roman", 10))
            user_label.grid(row=2, column=0, pady=10)
            info2_label = Label(add_new, text="What will be in the password slot?")
            info2_label.grid(row=6, column=0, pady=10)
            password_label = Label(add_new, text="Password", font=("Times New Roman", 10))
            password_label.grid(row=8, column=0, pady=10)
            info3_label = Label(add_new, text="What will be in the email slot? (You can leave it blank if you wish)")
            info3_label.grid(row=12, column=0, pady=10)
            email_label = Label(add_new, text="Email:", font=("Times New Roman", 10))
            email_label.grid(row=14, column=0, pady=10)
            info4_label = Label(add_new, text="What will be in the info slot? (You can leave it blank if you wish)")
            info4_label.grid(row=18, column=0, pady=10)
            info_label = Label(add_new, text="Info:", font=("Times New Roman", 10))
            info_label.grid(row=20, column=0, pady=10)

            # Create Entry
            user_entry = Entry(add_new, width=50)
            user_entry.grid(row=4, column=0)
            password_entry = Entry(add_new, width=50)
            password_entry.grid(row=10, column=0)
            email_entry = Entry(add_new, width=50)
            email_entry.grid(row=16, column=0)
            info_entry = Entry(add_new, width=50)
            info_entry.grid(row=22, column=0, ipady=10)

            # Command for button
            def submit_add():
                # Encrypts all the info given by the user
                encrypted_info = cryptographyDefFunc.encrypt_all(username, user_entry.get(), password_entry.get(), email_entry.get(), info_entry.get())

                # Gives the encrypted info to submit to the db (data base)
                password_keeper_def_func.add_one(username, encrypted_info[0], encrypted_info[1], encrypted_info[2],
                                                     encrypted_info[3])

                messagebox.showinfo(title="Done!", message="Password Added Correctly!")

                user_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                info_entry.delete(0, END)

            def go_back():
                add_new.destroy()
                root.deiconify()

            # Create Buttons
            submit_btn = Button(add_new, text="Add", command=submit_add)
            submit_btn.grid(row=26, column=0, pady=10)
            return_btn = Button(add_new, text="Return", command=go_back)
            return_btn.grid(row=27, column=0, pady=10)

        except Exception as error:
            messagebox.showerror("Error", error)

        add_new.mainloop()

    def search():
        top = Toplevel()
        top.title("Search...")
        top.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
        top.geometry(str(width) + "x" + str(height))
        top.geometry(str(width) + "x" + str(height) + "+" + str(x_coordinate) + "+" + str(y_coordinate))

        try:
            # Create a Tkinter Var
            clicked = StringVar()
            clicked.set("Choose a Searching Option")
            drop = OptionMenu(top, clicked, "ID", "Name", "Email")
            drop.grid(row=0, column=0, padx=5, pady=5)
            search_entry = Entry(top, width=30)
            search_entry.grid(row=0, column=10, padx=5, pady=5)
            def search():
                search_result = search_entry.get()
                if search_result == "":
                    messagebox.showerror("Error", "Searching field is empty. :/")

                if (clicked.get()=="ID"):
                    # Gets the key for the specified user
                    key = cryptographyDefFunc.get_key(username)
                    # Searches for a match in database
                    password_keeper_def_func.id_lookup(key, username, search_entry.get())
                    print("If blank, none where found.")
                elif (clicked.get() == "Name"):
                    # Gets the key for the specified user
                    key = cryptographyDefFunc.get_key(username)
                    # Searches for a match in database
                    password_keeper_def_func.name_lookup(key, username, search_entry.get())
                    print("If blank, none where found.")
                    pass
                elif clicked.get() == "Email":
                    # Gets the key for the specified user
                    key = cryptographyDefFunc.get_key(username)
                    # Searches for a match in database
                    password_keeper_def_func.email_lookup(key, username, search_entry.get())
                    print("If blank, none where found.")
                    pass
                else:
                    messagebox.showerror("Error", "Invalid Selection. Please try again.")
                show_label = Label(top, text=clicked.get()).grid(row=4, column=0, padx=5, pady=5)

            search_btn = Button(top, text="Search", command=search).grid(row=2, column=0, padx=5, pady=5)
            def go_back():
                top.destroy()

            return_btn = Button(top, text="Go Back", command=go_back)
            return_btn.grid(row=2, column=10, padx=5, pady=5)

            top.mainloop()
        except Exception as error:
            print(error)

    def edit():
        root.withdraw()
        add_new = Tk()
        add_new.title("Edit Password")
        add_new.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
        width2 = 350
        height2 = 300
        add_new.geometry(str(width2) + "x" + str(height2))
        x_coordinate2 = int((screen_width / 2) - (width2 / 2))
        y_coordinate2 = int((screen_height / 2) - (height2 / 2))
        add_new.geometry(str(width2) + "x" + str(height2) + "+" + str(x_coordinate2) + "+" + str(y_coordinate2))

        messagebox.showinfo("Info", "Once updated there is no going back")

        # Create Labels
        info0_label = Label(add_new, text="The ID of the record you wish to edit.")
        info0_label.grid(row=0, column=0, pady=10, padx=10)

        # Create Entry
        id_entry = Entry(add_new, width=50)
        id_entry.grid(row=4, column=0, padx=10, pady=10)

        # Command for button
        def edit_record():
            id_num_edit = id_entry.get()
            if id_entry.get() == "":
                messagebox.showerror("Error", "Invalid id")
            else:
                add_new.destroy()
                edit_new = Toplevel()
                edit_new.title("Edit Password")
                edit_new.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
                width3 = 500
                height3 = 600
                x_coordinate3 = int((screen_width / 2) - (width3 / 2))
                y_coordinate3 = int((screen_height / 2) - (height3 / 2))
                edit_new.geometry(str(width3) + "x" + str(height3))
                edit_new.geometry(str(width3) + "x" + str(height3) + "+" + str(x_coordinate3) + "+" + str(y_coordinate3))

                # Create Labels
                info1_label = Label(edit_new,
                                    text="What will be in the user field? (You can add the name of the website or the username, etc.)")
                info1_label.grid(row=0, column=0, pady=10)
                user_label = Label(edit_new, text="Username/Website URL:", font=("Times New Roman", 10))
                user_label.grid(row=2, column=0, pady=10)
                info2_label = Label(edit_new, text="What will be in the password slot?")
                info2_label.grid(row=6, column=0, pady=10)
                password_label = Label(edit_new, text="Password", font=("Times New Roman", 10))
                password_label.grid(row=8, column=0, pady=10)
                info3_label = Label(edit_new, text="What will be in the email slot? (You can leave it blank if you wish)")
                info3_label.grid(row=12, column=0, pady=10)
                email_label = Label(edit_new, text="Email:", font=("Times New Roman", 10))
                email_label.grid(row=14, column=0, pady=10)
                info4_label = Label(edit_new, text="What will be in the info slot? (You can leave it blank if you wish)")
                info4_label.grid(row=18, column=0, pady=10)
                info_label = Label(edit_new, text="Info:", font=("Times New Roman", 10))
                info_label.grid(row=20, column=0, pady=10)

                # Create Entry
                user_entry = Entry(edit_new, width=50)
                user_entry.grid(row=4, column=0)
                password_entry = Entry(edit_new, width=50)
                password_entry.grid(row=10, column=0)
                email_entry = Entry(edit_new, width=50)
                email_entry.grid(row=16, column=0)
                info_entry = Entry(edit_new, width=50)
                info_entry.grid(row=22, column=0, ipady=10)

                # Command for button
                def edit_add():
                    # Encrypts all the info given by the user
                    encrypted_info = cryptographyDefFunc.encrypt_all(username, user_entry.get(), password_entry.get(),
                                                                     email_entry.get(), info_entry.get())

                    password_keeper_def_func.update_one(username, encrypted_info[0], encrypted_info[1],
                                                        encrypted_info[2],
                                                        encrypted_info[3], id_num_edit)

                    messagebox.showinfo(title="Done!", message="Record Edited Successfully!")
                    go_back()

                def go_back():
                    edit_new.destroy()
                    root.deiconify()

                # Create Buttons
                submit_btn = Button(edit_new, text="Edit", command=edit_add)
                submit_btn.grid(row=26, column=0, pady=10)
                return_btn = Button(edit_new, text="Return", command=go_back)
                return_btn.grid(row=27, column=0, pady=10)

                edit_new.mainloop()

        def go_back():
            add_new.destroy()
            root.deiconify()

        # Create Buttons
        submit_btn = Button(add_new, text="Edit", command=edit_record)
        submit_btn.grid(row=26, column=0, pady=10)
        return_btn = Button(add_new, text="Return", command=go_back)
        return_btn.grid(row=27, column=0, pady=10)

        add_new.mainloop()

    def delete():
        root.withdraw()
        delete_record = Tk()
        delete_record.title("Delete Password")
        delete_record.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
        width2 = 350
        height2 = 300
        delete_record.geometry(str(width2) + "x" + str(height2))
        x_coordinate2 = int((screen_width / 2) - (width2 / 2))
        y_coordinate2 = int((screen_height / 2) - (height2 / 2))
        delete_record.geometry(str(width2) + "x" + str(height2) + "+" + str(x_coordinate2) + "+" + str(y_coordinate2))

        messagebox.showwarning("Warning", "Once deleted there is no going back!")

        # Create Labels
        info0_label = Label(delete_record, text="The ID of the record you wish to delete.")
        info0_label.grid(row=0, column=0, pady=10, padx=10)

        # Create Entry
        id_entry = Entry(delete_record, width=50)
        id_entry.grid(row=4, column=0, padx=10, pady=10)

        def go_back():
            delete_record.destroy()
            root.deiconify()

        def delete_passwrd():
            try:
                if messagebox.askokcancel("Sure tho?", "Are you sure you want to delete this record?") == 1:
                    id_var = id_entry.get()
                    print(id_entry.get())
                    print(type(id_entry.get()))
                    print(username)
                    print(type(username))
                    password_keeper_def_func.delete_one(username, id_var)
                    messagebox.showinfo("Info", "Record was deleted successfully.")
                else:
                    messagebox.showinfo("Info", "Transaction cancelled. Phew! That was a close one.")
                go_back()
            except Exception as error:
                print(error)
                messagebox.showerror("Error", error)

        # Create Buttons
        submit_btn = Button(delete_record, text="Delete", command=delete_passwrd)
        submit_btn.grid(row=26, column=0, pady=10)
        return_btn = Button(delete_record, text="Return", command=go_back)
        return_btn.grid(row=27, column=0, pady=10)

        delete_record.mainloop()

    def exit_program():
        root.destroy()
        bye = Tk()
        bye.title("BYE!")
        bye.iconbitmap("ExtraSupportContent/florestechnologylogo.ico")
        width = 500
        height = 530
        bye.geometry(str(width) + "x" + str(height))
        screen_width = bye.winfo_screenwidth()
        screen_height = bye.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        bye.geometry(str(width) + "x" + str(height) + "+" + str(x_coordinate) + "+" + str(y_coordinate))

        my_img = ImageTk.PhotoImage(Image.open("ExtraSupportContent/FloresTechnologyLogo.png"))
        my_label = Label(bye, image=my_img)
        my_label.pack()
        quit_button = Button(bye, text="Exit", command=bye.destroy)
        quit_button.pack()

        bye.mainloop()
        os.system('notepad ExtraSupportContent/about.txt')

    # Create Buttons
    view_pass_btn = Button(root, text="View Passwords", font=("Times New Roman", 13), command=view)
    view_pass_btn.grid(row=3, column=1, padx=10, pady=10)
    add_pass_btn = Button(root, text="Add Passwords", font=("Times New Roman", 13), command=add)
    add_pass_btn.grid(row=3, column=6, padx=10, pady=10)
    search_pass_btn = Button(root, text="Search for Passwords", font=("Times New Roman", 13), command=search)
    search_pass_btn.grid(row=5, column=1, padx=10, pady=10)
    edit_pass_btn = Button(root, text="Edit Passwords", font=("Times New Roman", 13), command=edit)
    edit_pass_btn.grid(row=5, column=6, padx=10, pady=10)
    delete_pass_btn = Button(root, text="Delete Passwords", font=("Times New Roman", 13), command=delete)
    delete_pass_btn.grid(row=7, column=3, padx=10, pady=10)
    exit_btn = Button(root, text="Exit", bg="black", fg="red", font=("Times New Roman", 13), command=exit_program)
    exit_btn.grid(row=10, column=3, pady=10)

    root.mainloop()
