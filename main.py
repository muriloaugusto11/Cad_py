import getpass

print("--||Cadastro||--")

name = input("Digite um nome: ")
while len(name) <3:
  print("Nome inválido, o tamanho mínimo de um nome deve ser 3 e você digitou:", len(name))
  name = input("Digite um nome válido: ")

cep = input("Digite um CEP: ")
address = input("Digite um endereço: ")

sex = input("Digite um sexo (Feminino/Masculino): " ).upper()
while sex != "F" and sex != "M" and sex != "FEMININO" and sex != "MASCULINO":
  print("Sexo Inválido!")
  sex = input("Digite seu Sexo (Feminino(F)/Masculino(M): ")
print(sex)

#(falta limitar a apenas números)
cpf = input("Digite um CPF válido: ")
while len(cpf) != 11:
  if len(cpf) < 11:
    print("Tamanho de CPF menor que o permitido!")
    print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
    cpf = input("Digite um CPF válido: ")
  if len(cpf) > 11:
    print("Tamanho de CPF maior que o permitido!")
    print("O campo CPF deve ter 11 caracteres e você forneceu: ", len(cpf))
    cpf = input("Digite um CPF válido: ")  

#(falta limitar a apenas números)
cel = input("Digite um celular válido: ")
while len(cel) != 11:
   print("Tamanho inválido, você forneceu", len(cel), "quando na verdade deve ser 11")
   cel = input("Digite o Celular válido: ")

#(falta limitar caracteres especiais)
login = input("Digite um Login válido: ")
while len(login) <3 or len(login) > 16:
  print("Login inválido, o Login deve ter no 3 caractéres e no máximo 16 caractéres e você forneceu: ", len(login))
  login = input("Digite um Login válido: ")

#(Falta obrigar uma letra maiuscula e uma mínima e aumentar o tamanho mínimo para 10)
password = input("Digite uma Senha válida: ")
while len(password) < 8 or len(password) > 16:
  print("Senha inválida, a Senha deve ter no mínimo 8 caractéres e no máximo 16 caractéres e você forneceu: ", len(password))
  password = input("Digite uma Senha válida: ")

c_password = input("Confirmação de Senha: ")
while password != c_password:
  print("As senhas não batem! Digite uma Senha novamente: ")
  password = input("Senha: ")
  c_password = input("Confirmação de Senha: ")
    
l_login = input("Digite um Login: ")    
p_password = getpass.getpass("Digite uma Senha: ")    
while l_login != login and p_password != password:
  print("Login ou Senha inválidos!")
  l_login = input("Digite um Login válido: ")
  p_password = getpass.getpass("Digite uma Senha válida: ")
  if l_login == login and p_password == password:
    print("ok")
  else:
    print()
