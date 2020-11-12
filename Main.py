import newUser
import firstRun
import existingUser

exit = False
while exit != True:
    print("\nWelcome to the password manager with encryption and database v1.")
    print("Options: \n"
          "1. Existing User\n"
          "2. New User\n"
          "3. First Run (IMPORTANT for first time runs)\n"
          "0. Exit\n"
          "---------------------------------------------------------------------------")
    startMenu = int(input("Enter option: "))
    if startMenu == 1:
        if existingUser.serchUser() == True:
            pass
        else:
            print("User has not been found. Please try again, or create an account.")
    elif startMenu == 2:
        newUser.signup()
    elif startMenu == 3:
        firstRun.tableCreate()
        print("\nDatabase has been created succesfully, you can now create a new account! :)\n")
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