import sqlite3
import getpass
import re
import io


def create_table():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS dados (id string, name string, cep string, address string, sex string, '
              'cpf string, cel string, login string, password string)')
    c.close()


create_table()


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


def register():
    print("\n REGISTER:")
    register_name()


def register_name():
    validation_name = input("TYPE A NAME: ")
    if len(validation_name) < 6:
        print("INVALID NAME, THE MINIMUM LENGTH OF A NAME SHOULD BE 6 AND YOU ENTERED:", len(validation_name))
        register_name()

    elif len(validation_name) >= 6:
        if re.match('^[a-zA-Z ]+$', validation_name):
            name = validation_name
            register_cep(name)

        else:
            print("INVALID NAME!")
            register_name()


def register_cep(name):
    validation_cep = input("TYPE A CEP: ")

    if len(validation_cep) < 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        register_cep(name)
    elif len(validation_cep) > 8:
        print("CEP FIELD MUST BE 8 CHARACTERS AND YOU PROVIDED: ", len(validation_cep))
        register_cep(name)
    elif len(validation_cep) == 8:
        if re.match('^[0-9]+$', validation_cep):
            cep = validation_cep
            register_address(name, cep)
        else:
            print("INVALID FORMAT")
            register_cep(name)


def register_address(name, cep):
    validation_address = input("TYPE AN ADDRESS: ")
    if re.match('^[a-zA-Z0-9 ]+$', validation_address):
        address = validation_address
        register_sex(name, cep, address)
    else:
        print("INVALID ADDRESS")
        register_address(name, cep)


def register_sex(name, cep, address):
    sex = input("ENTER A SEX (FEMALE(F)/MALE(M)/OTHER(O)): ").upper()
    while sex != "F" and sex != "M" and sex != "FEMALE" and sex != "MALE" and sex != "O":
        print("INVALID SEX!")
        sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")

    register_cpf(name, cep, address, sex)


def register_cpf(name, cep, address, sex):
    validation_cpf = input("ENTER A VALID CPF: ")
    if len(validation_cpf) != 11:
        print("CPF FIELD MUST BE 11 CHARACTERS AND YOU PROVIDED: ", len(validation_cpf))
        register_cpf(name, cep, address, sex)
    elif len(validation_cpf) == 11:
        if re.match('^[0-9]+$', validation_cpf):
            cpf = validation_cpf
            register_cel(name, cep, address, sex, cpf)
        else:
            print("INVALID FORMAT")
            register_cpf(name, cep, address, sex)


def register_cel(name, cep, address, sex, cpf):
    validation_cel = input("ENTER A VALID MOBILE NUMBER: ")
    if len(validation_cel) != 11:
        print("INVALID SIZE, YOU PROVIDE", len(validation_cel), "WHEN IN FACT IT SHOULD BE 11")
        register_cel(name, cep, address, sex, cpf)
    elif len(validation_cel) == 11:
        if re.match('^[0-9]+$', validation_cel):
            cel = validation_cel
            register_login(name, cep, address, sex, cpf, cel)
        else:
            print("INVALID PHONE NUMBER, YOU CANT USE SPECIAL CHARACTERS!")
            register_cel(name, cep, address, sex, cpf)


def register_login(name, cep, address, sex, cpf, cel):
    print("\n LOGIN REGISTER!")
    validation_login = input("ENTER A VALID LOGIN: ")
    if len(validation_login) < 3 or len(validation_login) > 16:
        print("INVALID LOGIN, LOGIN MUST BR IN 3 CHARACTERS AND A MAXIMUM OF 16 CHARACTERS AND YOU HAVE PROVIDED: ",
              len(validation_login))
        register_login(name, cep, address, sex, cpf, cel)
    elif len(validation_login) > 3 and len(validation_login) < 17:
        if re.match('^[a-zA-Z0-9_ ]+$', validation_login):
            login = validation_login
            register_password(name, cep, address, sex, cpf, cel, login)
        else:
            print("INVALID LOGIN, YOU CAN'T USE SPECIAL CHARACTERS!")
            register_login(name, cep, address, sex, cpf, cel)


def register_password(name, cep, address, sex, cpf, cel, login):
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    print("\n PASSWORD REGISTER!")
    validation_password = input("ENTER A VALID PASSWORD: ")
    c_password = input("ENTER A EQUAL AND VALID PASSWORD AGAIN TO CONFIRM: ")
    if validation_password == c_password:
        if len(validation_password) > 10 or len(validation_password) < 19:
            if re.match('^[a-zA-Z0-9_ ]+$', validation_password):
                password = validation_password
                print("SUCCESSFUL REGISTRATION!")

                c.execute('INSERT INTO dados VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)',
                          (3, name, cep, address, sex, cpf, cel, login, password))
                connection.commit()
                c.close()
                menu()

            else:
                print("YOU CAN'T USE SPECIAL CHARACTERES!")
                register_password(name, cep, address, sex, cpf, cel, login)
        else:
            print("INVALID SIZE")
            register_password(name, cep, address, sex, cpf, cel, login)
    else:
        print("THE PASSWORDS NOT MATCH")
        register_password(name, cep, address, sex, cpf, cel, login)


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


def read_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)
    c.close()
    adm_data()


def update_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)
    name = input("n:")
    cep = input("c:")
    address = input("a:")
    sex = input("s:")
    cpf = input("c:")
    cel = input("c:")
    login = input("l:")
    password = input("p:")
    id = input("i:")

    c.execute("""
    UPDATE dados
    SET name = ?, cep = ?, address = ?, sex = ?, cpf = ?, cel = ?, login = ?, password = ?
    WHERE id = ?
    """, (name, cep, address, sex, cpf, cel, login, password, id))
    connection.commit()
    c.close()
    read_data()
    adm_data()


def delete_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)
    id = input("D")
    c.execute("""
    DELETE FROM dados
    WHERE id = ?
    """, (id))
    connection.commit()
    c.close()
    read_data()
    adm_data()


def backup_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    with io.open('dados_dump.sql', 'w') as f:
        for dado in c.iterdump():
            f.write('%s\n' % dado)
    #cat clientes_dump.sql
    print('Backup realizado com sucesso.')
    print('Salvo como clientes_dump.sql')

    c.close()


def log_into():
    print("\n LOGIN:")
    l_login = input("\n ENTER A VALID LOGIN: ")
    p_password = getpass.getpass("\n ENTER A VALID PASSWORD: ")
    if l_login != login and p_password != password:
        print("\n INVALID LOGIN OR PASSWORD!")
        log_into()
    elif l_login == login and p_password == password:
        print("\n Logado!")
        menu()


menu()
