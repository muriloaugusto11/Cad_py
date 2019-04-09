import getpass
import re


def menu():

    print("\n Seja Bem Vindo!")
    opt = ""

    opt = int(input('\n MENU: ' +
                    '\n\n [1] - REGISTER: ' +
                    '\n [2] - LOG: ' +
                    '\n [3] - EXIT: \n \n '))

    if opt == 1:
        menu_register()

    elif opt == 2:
        menu_log()

    elif opt == 3:
        print("EXIT")

    elif opt == 4:
        register_login()


def menu_register():
    opt1 = int(input('\n REGISTRAR: ' +
                     '\n \n [1] - MANAGER: ' +
                     '\n [2] - EMPLOYEE: ' +
                     '\n [3] - CLIENT: ' +
                     '\n [4] - BACK TO MAIN MENU: \n \n'))
    if opt1 == 1:
        register()

    elif opt1 == 2:
        register()

    elif opt1 == 3:
        register()

    elif opt1 == 4:
        register_login()

    else:
        print("INVALID OPTION!")
        menu_register()


def menu_log():
    opt2 = int(input('\n LOGAR: ' +
                     '\n \n [1] - MANAGER: ' +
                     '\n [2] - EMPLOYEE: ' +
                     '\n [3] - BACK TO MAIN MENU: \n \n'))

    if opt2 == 1:
        menu_register()

    if opt2 == 2:
        menu_register()

    if opt2 == 3:
        menu_register()

    else:
        print("\n INVALID OPTION!")
        menu_log()


def register():
    print("\n REGISTER:")
    register_name()


def register_name():
    validation_name = input("TYPE A NAME: ")
    if len(validation_name) < 6:
        print("INVALID NAME, THE MINIMUM LENGTH OF A NAME SHOULD BE 6 AND YOU ENTERED:", len(validation_name))
        register_name()

    elif len(validation_name) > 6:
        if re.match('^[a-zA-Z ]+$', validation_name):
            name = validation_name
            register_cep()

        else:
            print("INVALID NAME!")
            register_name()


def register_cep():
    validation_cep = input("TYPE A CEP: ")

    if len(validation_cep) < 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        register_cep()
    elif len(validation_cep) > 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        register_cep()
    elif len(validation_cep) == 8:
        if re.match('^[0-9]+$', validation_cep):
            cep = validation_cep
            register_address()
        else:
            print("INVALID FORMAT")
            register_cep()


def register_address():
    validation_address = input("TYPE AN ADDRESS: ")
    if re.match('^[a-zA-Z0-9 ]+$', validation_address):
        address = validation_address
        register_sex()
    else:
        print("INVALID ADDRESS")
        register_address()


def register_sex():
    sex = input("ENTER A SEX (FEMALE(F)/MALE(M)): ").upper()
    while sex != "F" and sex != "M" and sex != "FEMALE" and sex != "MALE":
        print("INVALID SEX!")
        sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")

    register_cpf()


def register_cpf():
    validation_cpf = input("ENTER A VALID CPF: ")
    if len(validation_cpf) < 11:
        print("CPF FIELD MUST BE 11 CHARACTERS AND YOU PROVIDED: ", len(validation_cpf))
        register_cpf()
    elif len(validation_cpf) > 11:
        print("CPF FIELD MUST BE 11 CHARACTERS AND YOU PROVIDED: ", len(validation_cpf))
        register_cpf()
    elif len(validation_cpf) == 11:
        if re.match('^[0-9]+$', validation_cpf):
            cpf = validation_cpf
            register_cel()
        else:
            print("INVALID FORMAT")
            register_cpf()


def register_cel():
    validation_cel = input("ENTER A VALID MOBILE NUMBER: ")
    if len(validation_cel) != 11:
        print("INVALID SIZE, YOU PROVIDE", len(validation_cel), "WHEN IN FACT IT SHOULD BE 11")
        register_cel()
    elif len(validation_cel) == 11:
        if re.match('^[0-9]+$', validation_cel):
            cel = validation_cel
            register_login()
        else:
            print("INVALID PHONE NUMBER, YOU CANT USE SPECIAL CHARACTERS!")
            register_cel()


def register_login():
    print("\n LOGIN REGISTER!")
    validation_login = input("ENTER A VALID LOGIN: ")
    if len(validation_login) < 3 or len(validation_login) > 16:
        print("INVALID LOGIN, LOGIN MUST BR IN 3 CHARACTERS AND A MAXIMUM OF 16 CHARACTERS AND YOU HAVE PROVIDED: ",
              len(validation_login))
        register_login()
    elif len(validation_login) > 3 and len(validation_login) < 17:
        if re.match('^[a-zA-Z0-9_ ]+$', validation_login):
            login = validation_login
            register_password()
        else:
            print("INVALID LOGIN, YOU CAN'T USE SPECIAL CHARACTERS!")
            register_login()


def register_password():
    print("\n PASSWORD REGISTER!")
    password = input("ENTER A VALID PASSWORD: ")
    c_password = input("ENTER A EQUAL AND VALID PASSWORD AGAIN TO CONFIRM: ")
    if password == c_password:
        if len(password) > 10 or len(password) < 19:
            if re.match('^[a-zA-Z0-9_ ]+$', password):
                print("SUCESSEFULL REGISTRATION!")
                logar()

            else:
                print("YOU CAN'T USE SPECIAL CHARACTERES!")
                register_password()
        else:
            print("INVALID SIZE")
            register_password()
    else:
        print("THE PASSWORDS NOT MATCH")
        register_password()


def logar():
    print("\n LOGIN:")
    l_login = input("\n ENTER A VALID LOGIN: ")
    p_password = getpass.getpass("\n ENTER A VALID PASSWORD: ")
    if l_login != login and p_password != password:
        print("\n INVALID LOGIN OR PASSWORD!")
        logar()
    if l_login == login and p_password == password:
        print("\n Logado!")
        menu()


menu()
