import getpass

print("--||Cadastro||--")

#(Falta limitar campo nome)
name = input("Digite seu nome: ")
address = input("Digite seu endereço: ")
sex = input("Digite seu sexo (Feminino/Masculino): " ).upper()
while sex != "F" and sex != "M" and sex != "FEMININO" and sex != "MASCULINO":
  print("Sexo Inválido!")
  sex = input("Digite seu sexo (Feminino(F)/Masculino(M): ")
print(sex)

#(falta limitar a apenas números)
cpf = input("Digite seu cpf: ")
while len(cpf) != 11:
  if len(cpf) < 11:
    print("Tamanho de CPF menor que o permitido!")
    print("O campo CPF deve ter 11 caracteres e você forneceu", len(cpf))
    cpf = input("Digite seu cpf: ")
  if len(cpf) > 11:
    print("Tamanho de CPF maior que o permitido!")
    print("O campo CPF deve ter 11 caracteres e você forneceu", len(cpf))
    cpf = input("Digite novamente seu CPF: ")  

#(falta limitar a apenas números)
cel = input("Digite seu celular: ")
while len(cel) != 11:
   print("Tamanho inválido, você forneceu", len(cel), "quando na verdade deve ser 11, ")
   cel = input("Digite o número de celular novamente: ")

#(falta limitar caracteres especiais)
login = input("Digite um login: ")
while len(login) <3 or len(login) > 16:
  print("Login inválido, o login deve ter no 3 caractéres e no máximo 16 caractéres e voce forneceu", len(login))
  login = input("Digite um login novamente: ")

#(Falta obrigar uma letra maiuscula e uma mínima e aumentar o tamanho mínimo para 10)
password = input("Digite uma Senha: ")
while len(password) < 8 or len(password) > 16:
  print("Senha inválida, a senha deve ter no mínimo 8 caractéres e no máximo 16 caractéres e você forneceu", len(password))
  password = input("Digite uma Senha novamente: ")

c_password = input("Confirmação de senha: ")
while password != c_password:
  print("As senhas não batem! Digite novamente")
  password = input("Senha: ")
  c_password = input("Confirmação de senha: ")
    
l_login = input("Digite um login: ")    
p_password = getpass.getpass("Digite uma senha: ")    
while l_login != login and p_password != password:
  print("Login ou senha inválidos!")
  l_login = input("Digite um Login válido: ")
  p_password = getpass.getpass("Digite uma senha válida: ")
  if l_login == login and p_password == password:
    print("ok")
  else:
    print()
