# Uma empresa te contratou como programador e a sua primeira tarefa é: Criar um programa que solicite ao usuário a senha e solicite que digite-a novamente até que as duas sejam digitadas da mesma forma.

while True:
    senha = input("Digite uma senha: ")
    confirmar_senha = input("Digite a senha novamente: ")
    
    if senha == confirmar_senha:
        break
    else:
        print("Senha incorreta...")
        continue
