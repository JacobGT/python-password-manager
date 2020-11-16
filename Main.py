import newUserMain
import firstRunMain
import existingUserMain
import pswrdKprMain
import firstRunPswrdKpr
import sqlite3

exit = False
while exit != True:
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
        #try:
        if existingUserMain.searchUser(username, password) == True:
            print("User has been found")
            pswrdKprMain.mainPasswordKeeper(username)
        else:
            print("User has not been found. Please try again, or create an account.")
        #except:
        #    print("Error, database has not been created. Please run new user and try again.")
    elif startMenu == 2:
        try:
            firstRunMain.tableCreate()
        except sqlite3.OperationalError as error:
            print("")
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
        newUserMain.signup(username, password)
        pswrdKprMain.mainPasswordKeeper(username)
        firstRunPswrdKpr.createTable(username)
    else:
        exit = True
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