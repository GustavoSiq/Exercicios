# Faça um programa que permita ler vários números: Para sair do programa, será necessário digitar o número 0. Após sair, mostre quantos números foram digitados e qual foi a soma entre eles

lista = []
tamanho = 0
soma = 0

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    lista.append(n)

tamanho = len(lista)

print(tamanho)
