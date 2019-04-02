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
    cad_name()

def cad_name():
    validation_name = input("TYPE A NAME: ")
    if len(validation_name) < 6:
      print("Nome inválido, o tamanho mínimo de um nome deve ser 6 e você digitou:", len(validation_name))
      cad_name()

    elif len(validation_name) > 6:
      if re.match('^[a-zA-Z ]+$', validation_name): 
        name = validation_name
        print(name)
        cad_cep()
      else:
        print("Nome inválido!")
      cad_name()

def cad_cep():
    validation_cep = input("TYPE A CEP: ")
    if re.match('^[0-9]+$', validation_cep):
      cep = validation_cep
    else:
      print("CEP inválido!")
      cad_cep()
    cad_address()

def cad_address():
    validation_address = input("TYPE AN ADDRESS: ")
    if re.match('^[a-zA-Z ]+$', validation_address):
      address = validation_address
    else:
      print("Invalid Address")
      cad_address
    cad_sex()

def cad_sex():
    sex = input("ENTER A SEX (FEMALE(F)/MALE(M)): " ).upper()
    while sex != "F" and sex != "M" and sex != "FEMININO" and sex != "MASCULINO":
      print("INVALID SEX!")
      sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")
      print(sex)
    cad_cpf()

def cad_cpf():
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
      cad_cel()

def cad_cel():
    ##(falta limitar a apenas números)
    cel = input("ENTER A VALID MOBILE NUMBER: ")
    while len(cel) != 11:
      print("Tamanho inválido, você forneceu", len(cel), "quando na verdade deve ser 11")
      cel = input("ENTER A VALID MOBILE NUMBER: ")
    cad_login()

def cad_login():
    ##(falta limitar caracteres especiais)
    login = input("ENTER A VALID LOGIN: ")
    while len(login) <3 or len(login) > 16:
      print("Login inválido, o Login deve ter no 3 caractéres e no máximo 16 caractéres e você forneceu: ", len(login))
      login = input("ENTER A VALID LOGIN: ")
    cad_password()

def cad_password():
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
