# Import all necessary packages
import sqlite3  # Import sqlite for database
import main_def_func  # Define all the functions used here
import password_keeper  # Goes to another section where all the passwords are kept (encrypted)
import password_keeper_def_func  # Defines all functions for the password_keeper
import cryptographyDefFunc  # Defines all the functions for encrypting, decrypting getting and setting the keys, etc.

# We do a while menu so the program only ends when the user specifies to do so
exit = False
while exit != True:
    # Create a menu
    print("\nWelcome to the password manager with encryption and database v1.")
    print("Options: \n"
          "1. Existing User\n"
          "2. New User\n"
          "0. Exit\n"
          "---------------------------------------------------------------------------")
    startMenu = int(input("Enter option: "))
    if startMenu == 1:
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
        key = cryptographyDefFunc.get_key(username)  # Gets the key for the specified user
        try:
            # Because the username and password where encrypted when inserting into table we need to compare them
            if main_def_func.searchUser(key, username, password) == True:
                print("User has been found")
                password_keeper.mainPasswordKeeper(username)  # We give all the necessary parameters
            else:
                print("User has not been found. Please try again, or create an account.")
        except:
            print("Error, database has not been created. Please run new user and try again.")
    elif startMenu == 2:
        try:
            main_def_func.tableCreate()  # Searches to see if database has all ready been created
        except sqlite3.OperationalError as error:
            print("")
        username = str(input("Enter username: "))  # asks username
        password = str(input("Enter password: "))  # asks password
        cryptographyDefFunc.set_key(username)  # sets key for encryption for specified user
        encrypted_user = cryptographyDefFunc.encrypt_some(username, password)  # encrypts user and password
        encrypted_username = encrypted_user[0]
        encrypted_password = encrypted_user[1]
        main_def_func.signup(encrypted_username, encrypted_password)  # creates record in first table with encrypted data
        password_keeper.mainPasswordKeeper(username)  # We give all the necessary parameters
        password_keeper_def_func.createTable(username)  # Creates second table for that specified user
    else:
        exit = True  # Exits the program
        print("           ,aodObo," +
         "\n        ,AMMMMP~~~~" +
         "\n     ,MMMMMMMMA." +
         "\n  ,M;'     `YV'\n" +
         "  AM' ,OMA,\n" +
         " AM|   `~VMM,.      .,ama,____,amma,..\n" +
         " MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.\n" +
         " VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD\n" +
         " `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,\n" +
         "  VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM\n" +
         "  `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM\n" +
         "   AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM\n" +
         "  ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM\n" +
         "  AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM\n" +
         " ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM\n" +
         " AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM\n" +
         " VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM\n" +
         " `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM\n" +
         "    aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM\n" +
         "    VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM\n" +
         "    `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM\n" +
         "     AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM\n" +
         "       YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM\n" +
         "        YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM\n" +
         "       AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM\n" +
         "       `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM\n" +
         "     ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM\n" +
         "   ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n" +
         " ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n" +
         "AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMM            -JacobGT")