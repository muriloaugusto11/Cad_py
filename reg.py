import sqlite3
import getpass
import re
import io
global id_i
id_i = 0


def create_table():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS dados (id_i integer PRIMARY KEY AUTOINCREMENT, name string,'
              ' cep string, address string, sex string, cpf string, cel string, login string, password string)')
    c.close()


create_table()


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
                          (id_i, name, cep, address, sex, cpf, cel, login, password))
                connection.commit()
                c.close()


            else:
                print("YOU CAN'T USE SPECIAL CHARACTERES!")
                register_password(name, cep, address, sex, cpf, cel, login)
        else:
            print("INVALID SIZE")
            register_password(name, cep, address, sex, cpf, cel, login)
    else:
        print("THE PASSWORDS NOT MATCH")
        register_password(name, cep, address, sex, cpf, cel, login)


def read_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)
    c.close()


def update_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)

    print("\n Digite o nome da coluna que deseja alterar: ")
    alter_option = int(input(' [0] - Name: ' +
                         '\n [1] - Cep: ' +
                         '\n [2] - Address: ' +
                         '\n [3] - Sex: ' +
                         '\n [4] - Cpf: ' +
                         '\n [5] - Cel: ' +
                         '\n [6] - Login: ' +
                         '\n [7] - Password: ' +
                         '\n [8] - EXIT: \n \n'))


    value_option = input("Digite o novo valor: ")
    key_option = input("Digite o nome da chave que deseja alterar: ")
    colunas = ["name", "cep", "address", "sex", "cpf", "cel", "login", "password"]
    #ids = ["id_i"]
    alter_option = colunas[alter_option]
    print(alter_option)
    for col in colunas:
        if col == alter_option:
            c.execute("""
            UPDATE dados
            SET """ + alter_option + """ = ?
            WHERE id_i = """ + key_option, (value_option,))
            connection.commit()
            c.close()
            read_data()



'''''''''               
    name = input("n:")
    cep = input("c:")
    address = input("a:")
    sex = input("s:")
    cpf = input("c:")
    cel = input("c:")
    login = input("l:")
    password = input("p:")
    id_i = input("i:")
    c.execute("""
    UPDATE dados
    SET name = ?, cep = ?, address = ?, sex = ?, cpf = ?, cel = ?, login = ?, password = ?
    WHERE id_i = ?
    """, (name, cep, address, sex, cpf, cel, login, password, id_i))
    connection.commit()
    c.close()
    read_data()
    adm_data()
'''''


def delete_data():
    connection = sqlite3.connect('cadastro.db')
    c = connection.cursor()

    c.execute("""
    SELECT * FROM dados;
    """)

    for dado in c.fetchall():
        print(dado)
    id_i = input("D")
    c.execute("""
    DELETE FROM dados
    WHERE id_i = ?
    """, (id_i))
    connection.commit()
    c.close()
    read_data()


def backup_data():
    c = sqlite3.connect('cadastro.db')

    with io.open('dados_dump.sql', 'w') as f:
        for dado in c.iterdump():
            f.write('%s\n' % dado)
    #cat clientes_dump.sql
    print('Success Backup.')
    print('Save with clientes_dump.sql')

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
