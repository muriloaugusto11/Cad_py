import getpass

print("--||Cadastro||--")

#nome = input("Digite seu nome: ")
#endereço = input("Digite seu endereço: ")
#sexo = input("Digite seu sexo (Feminino/Masculino): " ).upper()
#while sexo != "F" and sexo != "M" and sexo != "FEMININO" and sexo != "MASCULINO":
#  print("Sexo Inválido!")
#  sexo = input("Digite seu sexo (Feminino(F)/Masculino(M): " )
#print(sexo)
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

celular = input("Digite seu celular: ")
senha = input("")
conf_senha = input("")

senha = getpass.getpass("Digite sua senha de acesso: ")
while senha != '123321':
  if senha == '123321':
    print()
  else:
    senha = getpass.getpass("Digite uma senha válida: ")
print("Seja bem vindo!")

