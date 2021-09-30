# Escreva um programa que leia um número e mostre o seu fatorial.
# Exemplo: Número 5 = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input("Informe o número: "))

print(f"O fatorial de {num} é: {factorial(num)}")