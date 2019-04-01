import getpass

print("--||Cadastro||--")

#nome = input("Digite seu nome: ")
#endereço = input("Digite seu endereço: ")
#sexo = input("Digite seu sexo (Feminino/Masculino): " ).upper()
#while sexo != "F" and sexo != "M" and sexo != "FEMININO" and sexo != "MASCULINO":
#  print("Sexo Inválido!")
#  sexo = input("Digite seu sexo (Feminino(F)/Masculino(M): " )
#print(sexo)

#(falta limitar a apenas números)
#cpf = input("Digite seu cpf: ")
#while len(cpf) != 11:
#  if len(cpf) < 11:
#    print("Tamanho de CPF menor que o permitido!")
#    print("O campo CPF deve ter 11 caracteres e você forneceu", len(cpf))
#    cpf = input("Digite seu cpf: ")
#  if len(cpf) > 11:
#    print("Tamanho de CPF maior que o permitido!")
#    print("O campo CPF deve ter 11 caracteres e você forneceu", len(cpf))
#    cpf = input("Digite novamente seu CPF: ")  

#(falta limitar a apenas números)
#celular = input("Digite seu celular: ")
#while len(celular) != 11:
#  print("Tamanho inválido, você forneceu", len(celular),
#   "quando na verdade deve ser 11, ")
#  celular = input("Digite o número de celular novamente: ")

senha = input("Senha: ")
conf_senha = input("Confirmação de senha: ")
while senha != conf_senha:
  print("As senhas não batem! Digite novamente")
  senha = input("Senha: ")
  conf_senha = input("Confirmação de senha: ")

senha = getpass.getpass("Digite sua senha de acesso: ")
while senha != '123321':
  if senha == '123321':
    print()
  else:
    senha = getpass.getpass("Digite uma senha válida: ")
print("Seja bem vindo!")
