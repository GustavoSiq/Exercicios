#Questão c.

acesso = True

while acesso:
    nome = input("Informe um nome: ")
    senha = input("Informe uma senha: ")

    if senha == nome:
        print("Senha Inválida, digite uma senha diferente do nome...")
    else:
        break

print("Hello, world!")