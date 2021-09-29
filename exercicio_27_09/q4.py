# Faça um programa que solicite um número inteiro e mostre a tabuada de 1 a 10 do valor informado.

n = int(input("Informe o número: "))
counter = 1

while counter <= 10:
    resultado = n * counter
    print(f"{n} x {counter} = {resultado}")
    counter += 1