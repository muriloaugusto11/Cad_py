import getpass
import re


def menu():
    opt = ""
    while opt != 3:
        
        opt = int(input('\n [1] - CAD: ' +
                        '\n [2] - LOG: ' +
                        '\n [3] - EXIT: \n \n '))

        if opt == 1:
            cad()

        elif opt == 2:
            logar()

        elif opt == 3:
            print("\n END PROGRAM!")

        else:
            print("INVALID OPTION!")


def cad():
    print("\n REGISTER:")
    cad_name()


def cad_name():
    validation_name = input("TYPE A NAME: ")
    if len(validation_name) < 6:
        print("INVALID NAME, THE MINIMUM LENGTH OF A NAME SHOULD BE 6 AND YOU ENTERED:", len(validation_name))
        cad_name()

    elif len(validation_name) > 6:
        if re.match('^[a-zA-Z ]+$', validation_name):
            name = validation_name
            cad_cep()
        else:
            print("INVALID NAME!")
            cad_name()


def cad_cep():
    validation_cep = input("TYPE A CEP: ")

    if len(validation_cep) < 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        cad_cep()
    elif len(validation_cep) > 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        cad_cep()
    elif len(validation_cep) == 8:
        if re.match('^[0-9]+$', validation_cep):
            cef = validation_cep
            cad_address()
        else:
            print("INVALID FORMAT")
            cad_cep()


def cad_address():
    validation_address = input("TYPE AN ADDRESS: ")
    if re.match('^[a-zA-Z0-9 ]+$', validation_address):
        address = validation_address
        cad_sex()
    else:
        print("INVALID ADDRESS")
        cad_address()


def cad_sex():
    sex = input("ENTER A SEX (FEMALE(F)/MALE(M)): ").upper()
    while sex != "F" and sex != "M" and sex != "FEMALE" and sex != "MALE":
        print("INVALID SEX!")
        sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")

    cad_cpf()


def cad_cpf():
    validation_cpf = input("ENTER A VALID CPF: ")
    if len(validation_cpf) < 11:
        print("CPF FIELD MUST BE 11 CHARACTERS AND YOU PROVIDED: ", len(validation_cpf))
        cad_cpf()
    elif len(validation_cpf) > 11:
        print("CPF FIELD MUST BE 11 CHARACTERS AND YOU PROVIDED: ", len(validation_cpf))
        cad_cpf()
    elif len(validation_cpf) == 11:
        if re.match('^[0-9]+$', validation_cpf):
            cpf = validation_cpf
            cad_cel()
        else:
            print("INVALID FORMAT")
            cad_cpf()


def cad_cel():
    validation_cel = input("ENTER A VALID MOBILE NUMBER: ")
    if len(validation_cel) != 11:
        print("INVALID SIZE, YOU PROVIDE", len(validation_cel), "WHEN IN FACT IT SHOULD BE 11")
        cad_cel()
    elif len(validation_cel) == 11:
        if re.match('^[0-9]+$', validation_cel):
            cel = validation_cel
            cad_login()
        else:
            print("INVALID PHONE NUMBER, YOU CANT USE SPECIAL CHARACTERS!")
            cad_cel()


def cad_login():
    validation_login = input("ENTER A VALID LOGIN: ")
    if len(validation_login) < 3 or len(validation_login) > 16:
        print("INVALID LOGIN, LOGIN MUST BR IN 3 CHARACTERS AND A MAXIMUM OF 16 CHARACTERS AND YOU HAVE PROVIDED: ", len(validation_login))
        cad_login()
    elif len(validation_login) > 3 and len(validation_login) < 17:
        if re.match('^[a-zA-Z0-9_ ]+$', validation_login):
            login = validation_login
            cad_password()
        else:
            print("INVALID LOGIN, YOU CAN'T USE SPECIAL CHARACTERS!")
            cad_login()


def cad_password():
    print("Cadastro de Senha!")
    pw()


def pw():
    password = input("ENTER A VALID PASSWORD: ")
    c_password = input("ENTER A EQUAL AND VALID PASSWORD AGAIN TO CONFIRM: ")
    if password == c_password:
        if len(password) > 10 or len(password) < 19:
            if re.match('^[a-zA-Z0-9_ ]+$', password):
                print("SUCESSEFULL REGISTRATION!")
                menu()
            else:
                print("YOU CAN'T USE SPECIAL CHARACTERES!")
                pw()
        else:
            print("INVALID SIZE")
            pw()
    else:
        print("THE PASSWORDS NOT MATCH")
        pw()

    menu()

def logar():
    print("\n Login:")

    l_login = input("ENTER A VALID LOGIN: ")
    p_password = getpass.getpass("ENTER A VALID PASSWORD: ")
    if l_login != login and p_password != password:
        print("INVALID LOGIN OR PASSWORD!")
        logar()
    if l_login == login and p_password == password:
        print("Logado!")

menu()
