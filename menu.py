from reg import *


def menu():
    print("\n Welcome!")
    opt = int(input('\n MENU: ' +
                    '\n \n [1] - REGISTER CLIENT: ' +
                    '\n [2] - LOG INTO: ' +
                    '\n [3] - MANAGER CRUD: ' +
                    '\n [4] - EXIT: \n \n'))

    if opt == 1:
        register()

    elif opt == 2:
        menu_log()

    elif opt == 3:
        adm_data()

    elif opt == 4:
        print("End Program")


def menu_log():
    opt2 = int(input('\n LOGIN: ' +
                     '\n \n [1] - MANAGER: ' +
                     '\n [2] - BACK TO MAIN MENU: \n \n'))

    if opt2 == 1:
        log_into()

    elif opt2 == 3:
        menu()

    else:
        print("\n INVALID OPTION!")
        menu_log()


def adm_data():
    print("\n Welcome!")

    opt = int(input('\n ADM: ' +
                    '\n \n [1] - READ(Only ADM): \n' +
                    '\n [2] - UPDATE(Only ADM): \n' +
                    '\n [3] - DELETE(Only ADM): \n' +
                    '\n [4] - BACKUP(Only ADM): \n' +
                    '\n [5] - MAIN MENU: \n \n'))

    if opt == 1:
        read_data()

    elif opt == 2:
        update_data()

    elif opt == 3:
        delete_data()

    elif opt == 4:
        backup_data()

    elif opt == 5:
        menu()


menu()
