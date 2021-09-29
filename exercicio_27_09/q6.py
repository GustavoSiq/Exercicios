# Faça um programa que informe um número inteiro e calcule a soma de todos os números de 1 até o número digitado.Por exemplo:

n = int(input("Informe um número: "))
valor = 0
contador = 1

while contador <= n:
    valor += contador
    contador += 1
    
print(valor)