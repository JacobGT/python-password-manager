import password_keeper_def_func  # Defines all the functions used in password_keeper
import cryptographyDefFunc  # Defines all the functions for encrypting, decrypting getting and setting the keys, etc.
import sqlite3  # Import sqlite for database

def mainPasswordKeeper(username):
    # Simple menu with while loop
    exit = False
    while exit != True:
        print("\nWelcome ", username)
        print("""Options:
        1. View passwords
        2. Add passwords
        3. Search for password
        4. Edit passwords
        5. Delete passwords
        0. Exit
        ------------------------------------------------------
        """)
        option = int(input("Choose option: "))

        if option == 1:
            try:
                # Gets the key for the specified user
                key = cryptographyDefFunc.get_key(username)
                # Shows all passwords, usernames, emails and info + rowid
                password_keeper_def_func.show_all(key, username)
            except:
                print("Unknown error, please try again later.")
        elif option == 2:
            try:
                # Sees if table has all ready been created
                password_keeper_def_func.createTable(username)
            except sqlite3.OperationalError:
                print("")

            try:
                # Asks user for all the info needed
                print("What will be in the user slot? (You can add the name of the website or the username, etc.)")
                user = str(input("Enter user/website: "))
                print("What will be in the password slot?")
                password = str(input("Enter password: "))
                print("What will be in the email slot? (You can leave it blank if you wish)")
                email = str(input("Enter email: "))
                print("What will be in the info slot? (You can leave it blank if you wish)")
                info = str(input("Enter info: "))

                # Encrypts all the info given by the user
                encrypted_info = cryptographyDefFunc.encrypt_all(username, user, password, email, info)

                # Gives the encrypted info to submit to the db (data base)
                password_keeper_def_func.add_one(username, encrypted_info[0], encrypted_info[1], encrypted_info[2], encrypted_info[3])
                print("Info added correctly.")
            except:
                print("Whoops, that didnt work...    :/")

        elif option == 3:
            try:
                # Asks the user for the info needed to search for the record
                print("What is the user you wish to lookup for? (Remember, in the user slot normally there goes the username/website)")
                name = input("Enter user/website: ")

                # Gets the key for the specified user
                key = cryptographyDefFunc.get_key(username)
                # Searches for a match in database
                password_keeper_def_func.name_lookup(key, username, name)
                print("If blank, none where found.")
            except:
                print("Unknown error, please try again.")

        elif option == 4:
            try:
                # Asks the user for the id of the record they wishes to change
                print("What is the id of the record you want to update? (Once updated there is no going back)")
                id = input("Enter id: ")
                # Asks to the user for the new info
                print("What will be in the user slot? (You can add the name of the website or the username, etc.)")
                user = str(input("Enter user/website: "))
                print("What will be in the password slot?")
                password = str(input("Enter password: "))
                print("What will be in the email slot? (You can leave it blank if you wish)")
                email = str(input("Enter email: "))
                print("What will be in the info slot? (You can leave it blank if you wish)")
                info = str(input("Enter info: "))

                # Encrypts all the info given by the user
                encrypted_info = cryptographyDefFunc.encrypt_all(username, user, password, email, info)

                password_keeper_def_func.update_one(username, encrypted_info[0], encrypted_info[1], encrypted_info[2], encrypted_info[3], id)
                print("Record edited successfully.")
            except:
                print("Something went wrong... but tbh I dont know where... we probably should call a professional.")

        elif option == 5:
            try:
                # Asks the user for id number and if they are sure
                print("Use the id to delete the record. Warning: when deleted, it CAN NOT come back.")
                id = str(input("Enter id: "))
                confirmation = input("Are you sure? (Y/N)   ")
                if confirmation == "Y" or confirmation == "y":
                    password_keeper_def_func.delete_one(username, id)
                    print("Record was deleted succesfully.")
                else:
                    print("Transaction cancelled. Phew! That was a close one.")
            except:
                print("Theere is no record with the id given. Try with another id.")

        else:
            # Return to main login/signup page
            exit = True
