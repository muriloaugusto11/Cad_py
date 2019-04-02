import getpass
import re

def menu():

  opt = ""
  while opt != "3":
    opt = input('\n [1] - CAD: ' +
                '\n [2] - LOG: ' +
                '\n [3] - EXIT: \n \n ')

    if opt == "1":
      cad()
    elif opt == "2":
      logar()
    elif opt == "3":
      print("\n Programa finalizado")
    else:
      print("Opção inválida")

def cad():
    print("\n Cadastro:")
    name()

def name():
    name_test = input("TYPE A NAME: ")
    
    if re.match('^[a-zA-Z0-9_]+$',name_test): 
      name = name_test
      cep()
    else:
      print("Nome inválido!")
      name()

    while len(name) < 6:
      print("Nome inválido, o tamanho mínimo de um nome deve ser 6 e você digitou:", len(name))
      name = input("TYPE A VALID NAME: ")

def cep():
    cep = input("TYPE A CEP: ")
    address()

def address():
    address = input("TYPE AN ADDRESS: ")
    sex()

def sex():
    sex = input("ENTER A SEX (FEMALE(F)/MALE(M)): " ).upper()
    while sex != "F" and sex != "M" and sex != "FEMININO" and sex != "MASCULINO":
      print("INVALID SEX!")
      sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")
      print(sex)
    cpf()

def cpf():
    ##(falta limitar a apenas números)
    cpf = int(input("ENTER A VALID CPF: "))

    while len(cpf) != 11:
      
      if len(cpf) < 11:
        print("Tamanho de CPF menor que o permitido!")
        print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
        cpf = input("ENTER A VALID CPF: ")
      if len(cpf) > 11:
        print("Tamanho de CPF maior que o permitido!")
        print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
        cpf = input("ENTER A VALID CPF: ")  
      cel()

def cel():
    ##(falta limitar a apenas números)
    cel = input("ENTER A VALID MOBILE NUMBER: ")
    while len(cel) != 11:
      print("Tamanho inválido, você forneceu", len(cel), "quando na verdade deve ser 11")
      cel = input("ENTER A VALID MOBILE NUMBER: ")
    login()

def login():
    ##(falta limitar caracteres especiais)
    login = input("ENTER A VALID LOGIN: ")
    while len(login) <3 or len(login) > 16:
      print("Login inválido, o Login deve ter no 3 caractéres e no máximo 16 caractéres e você forneceu: ", len(login))
      login = input("ENTER A VALID LOGIN: ")
    password()

def password():
    ##(Falta obrigar uma letra maiuscula e uma mínima e aumentar o tamanho mínimo para 10)
    password = input("ENTER A VALID PASSWORD: ")
    while len(password) < 8 or len(password) > 16:
      print("Senha inválida, a Senha deve ter no mínimo 8 caractéres e no máximo 16 caractéres e você forneceu: ", len(password))
      password = input("ENTER A VALID PASSWORD: ")

    c_password = input("ENTER A VALID PASSWORD AGAIN TO CONFIRM: ")
    while password != c_password:
      print("PASSWORDS DO NOT MATCH! ENTER A PASSWORD AGAIN: ")
      password = input("PASSWORD: ")
      c_password = input("PASSWORD CONFIRMATION: ")
    menu()

def logar():

  print("\n Login")
  #login = cad()
  #password = cad()
  l_login = input("ENTER A LOGIN: ")    
  p_password = getpass.getpass("ENTER A PASSWORD: ")    
  while l_login != login and p_password != password:
    print("INVALID LOGIN OR PASSWORD!")
    l_login = input("ENTER A VALID LOGIN: ")
    p_password = getpass.getpass("ENTER A VALID PASSWORD: ")
    if l_login == login and p_password == password:
      print("Corretos")
    else:
      print()

menu()
