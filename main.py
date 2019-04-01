import getpass

print("--||Cadastro||--")

#(Falta limitar campo nome)
nome = input("Digite seu nome: ")
endereço = input("Digite seu endereço: ")
sexo = input("Digite seu sexo (Feminino/Masculino): " ).upper()
while sexo != "F" and sexo != "M" and sexo != "FEMININO" and sexo != "MASCULINO":
  print("Sexo Inválido!")
  sexo = input("Digite seu sexo (Feminino(F)/Masculino(M): " )
print(sexo)

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
celular = input("Digite seu celular: ")
while len(celular) != 11:
   print("Tamanho inválido, você forneceu", len(celular), "quando na verdade deve ser 11, ")
   celular = input("Digite o número de celular novamente: ")

#(falta limitar caracteres especiais)
login = input("Digite um login: ")
while len(login) <3 or len(login) > 16:
  print("Login inválido, o login deve ter no 3 caractéres e no máximo 16 caractéres e voce forneceu", len(login))
  login = input("Digite um login novamente: ")

#(Falta obrigar uma letra maiuscula e uma mínima e aumentar o tamanho mínimo para 10)
senha = input("Digite uma Senha: ")
while len(senha) < 8 or len(senha) > 16:
  print("Senha inválida, a senha deve ter no mínimo 8 caractéres e no máximo 16 caractéres e você forneceu", len(senha))
  senha = input("Digite uma Senha novamente: ")

conf_senha = input("Confirmação de senha: ")
while senha != conf_senha:
  print("As senhas não batem! Digite novamente")
  senha = input("Senha: ")
  conf_senha = input("Confirmação de senha: ")
    
l_login = input("Digite um login: ")    
l_senha = getpass.getpass("Digite uma senha: ")    
while l_login != login and l_senha != senha:
  print("Login ou senha inválidos!")
  l_login = input("Digite um Login válido: ")
  l_senha = getpass.getpass("Digite uma senha válida: ")
  if l_login == login and l_senha == senha:
    print("ok")
  else:
    print()
