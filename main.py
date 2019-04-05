import getpass
import re


def menu():
    opt = ""
        
    opt = int(input('\n MENU: ' +
                    '\n [1] - REGISTER: ' +
                    '\n [2] - LOG: ' +
                    '\n [3] - EXIT: \n \n '))

    if opt == 1:
        opt1 = int(input('\n REGISTRAR: ' + 
                         '\n [1] - Gerente: ' +
                         '\n [2] - Funcionário: ' +
                         '\n [3] - Cliente: ' +
                         '\n [4] - Voltar: \n \n'))
        if opt1 == 1:
          print("Gerente Aqui")

        elif opt1 == 2:
          print("Funcionário Aqui")

        elif opt1 == 3:
          print("cliente")

        elif opt1 == 4:
          menu()

        else:
          print("invalid")

    elif opt == 2:
        opt2 = int(input('\n LOGAR: ' +
                         '\n [1] - Gerente: ' +
                         '\n [2] - Funcionário: ' +
                         '\n [3] - Voltar: \n \n'))
        if opt2 == 1:
            print("Gerente")

        if opt2 == 2:
            print("Funcionário")

        if opt2 == 3:
            menu()

    elif opt == 3:
        print("\n END PROGRAM!")

    else:
        print("\n INVALID OPTION!")


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
    validation_login = input("ENTER A VALID LOGIN: ")
    if len(validation_login) < 3 or len(validation_login) > 16:
        print("INVALID LOGIN, LOGIN MUST BR IN 3 CHARACTERS AND A MAXIMUM OF 16 CHARACTERS AND YOU HAVE PROVIDED: ", len(validation_login))
        register_login()
    elif len(validation_login) > 3 and len(validation_login) < 17:
        if re.match('^[a-zA-Z0-9_ ]+$', validation_login):
            login = validation_login
            register_password()
        else:
            print("INVALID LOGIN, YOU CAN'T USE SPECIAL CHARACTERS!")
            register_login()


def register_password():
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
