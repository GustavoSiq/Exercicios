# Solicite ao usuário que informe um número inteiro e informe se o número é positivo, negativo ou neutro.

n = int(input("Informe um número inteiro: "))

if n > 0:
    print(f"{n} é positivo!")
elif n < 0:
    print(f"{n} é negativo!")
else:
    print(f"{n} é neutro!")

