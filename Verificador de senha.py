senha = input("Digite sua senha: ")

tem_numero = False
for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
    print("Regras:")
    print("A senha precisa ter no mínimo 8 caracteres")
    print("A senha precisa ter pelo menos um número")





