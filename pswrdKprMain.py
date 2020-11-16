import defPsrdKpr
import firstRunPswrdKpr
import sqlite3

def mainPasswordKeeper(username):
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
            defPsrdKpr.show_all(username)
        elif option == 2:
            try:
                firstRunPswrdKpr.createTable(username)
            except sqlite3.OperationalError:
                print("")
            print("What will be in the user slot? (You can add the name of the website or the username, etc.)")
            user = str(input("Enter user/website: "))
            print("What will be in the password slot?")
            password = str(input("Enter password: "))
            print("What will be in the email slot? (You can leave it blank if you wish)")
            email = str(input("Enter email: "))
            print("What will be in the info slot? (You can leave it blank if you wish)")
            info = str(input("Enter info: "))
            defPsrdKpr.add_one(username, user, password, email, info)
            print("Info added correctly.")
        elif option == 3:
            print("What is the user you wish to lookup for? (Remember, in the user slot normally there goes the username/website)")
            name = input("Enter user/website: ")
            defPsrdKpr.name_lookup(username, name)
            print("If blank, none where found.")
        elif option == 4:
            print("What is the id of the record you want to update? (Once updated there is no going back)")
            id = input("Enter id: ")
            print("What will be in the user slot? (You can add the name of the website or the username, etc.)")
            user = str(input("Enter user/website: "))
            print("What will be in the password slot?")
            password = str(input("Enter password: "))
            print("What will be in the email slot? (You can leave it blank if you wish)")
            email = str(input("Enter email: "))
            print("What will be in the info slot? (You can leave it blank if you wish)")
            info = str(input("Enter info: "))
            defPsrdKpr.update_one(username, user, password, email, info, id)
            print("Record edited succesfully.")
        elif option == 5:
            print("Use the id to delete the record. Warning: when deleted, it CAN NOT come back.")
            id = str(input("Enter id: "))
            defPsrdKpr.delete_one(username, id)
            print("Record was deleted succesfully.")
        else:
            exit = True
