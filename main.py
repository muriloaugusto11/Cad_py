import getpass

def cad():

    print("_\|/__Cadastro__\|/_")
    print("_/|\__Alternat__/|\_")

    pass_login_list = []
    #name = input("TYPE A NAME: ")
    #while len(name) <3:
    #  print("Nome inválido, o tamanho mínimo de um nome deve ser 3 e você digitou:", len(name))
    #  name = input("TYPE A VALID NAME: ")

    #cep = input("TYPE A CEP: ")
    #print(cep)
    #address = input("TYPE AN ADDRESS: ")
    #print(address)

    #sex = input("ENTER A SEX (FEMALE(F)/MALE(M)): " ).upper()
    #while sex != "F" and sex != "M" and sex != "FEMININO" and #sex != "MASCULINO":
    #  print("INVALID SEX!")
    #  sex = input("ENTER THE SEX (FEMALE(F)/MALE(M): ")
    #  print(sex)

    ##(falta limitar a apenas números)
    #cpf = input("ENTER A VALID CPF: ")
    #while len(cpf) != 11:
    #  if len(cpf) < 11:
    #    print("Tamanho de CPF menor que o permitido!")
    #    print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
    #    cpf = input("ENTER A VALID CPF: ")
    #  if len(cpf) > 11:
    #    print("Tamanho de CPF maior que o permitido!")
    #    print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
    #    cpf = input("ENTER A VALID CPF: ")  

    ##(falta limitar a apenas números)
    #cel = input("ENTER A VALID MOBILE NUMBER: ")
    #while len(cel) != 11:
    #  print("Tamanho inválido, você forneceu", len(cel), "quando na verdade deve ser 11")
    #  cel = input("ENTER A VALID MOBILE NUMBER: ")

    ##(falta limitar caracteres especiais)
    login = input("ENTER A VALID LOGIN: ")
    while len(login) <3 or len(login) > 16:
      print("Login inválido, o Login deve ter no 3 caractéres e no máximo 16 caractéres e você forneceu: ", len(login))
      login = input("ENTER A VALID LOGIN: ")

    #(Falta obrigar uma letra maiuscula e uma mínima e aumentar o tamanho mínimo para 10)
    password = input("ENTER A VALID PASSWORD: ")
    while len(password) < 8 or len(password) > 16:
      print("Senha inválida, a Senha deve ter no mínimo 8 caractéres e no máximo 16 caractéres e você forneceu: ", len(password))
      password = input("ENTER A VALID PASSWORD: ")

    c_password = input("ENTER A VALID PASSWORD AGAIN TO CONFIRM: ")
    while password != c_password:
      print("PASSWORDS DO NOT MATCH! ENTER A PASSWORD AGAIN: ")
      password = input("PASSWORD: ")
      c_password = input("PASSWORD CONFIRMATION: ")

    pass_login_list.append(password + "-" + login) 
    print(pass_login_list)
def log():

    print(login)
    print(password)
    #l_login = input("ENTER A LOGIN: ")    
    #p_password = getpass.getpass("ENTER A PASSWORD: ")    
    #while l_login != login and p_password != password:
    #  print("INVALID LOGIN OR PASSWORD!")
    #  l_login = input("ENTER A VALID LOGIN: ")
    #  p_password = getpass.getpass("ENTER A VALID PASSWORD: ")
    #  if l_login == login and p_password == password:
    #    print("Corretos")
    #  else:
    #    print()

cad()

a = "0"
while a != "S" and a != "N":
  a = input("Deseja cadastrar mais um usuário? S/N ou Login L: ").upper()
  if a == "S":
    cad()
  elif a == "N":
    print("xs")
  elif a == "L":
    log()

  
