# Faça um programa que permite ler um número e escolhar uma das seguintes conversões:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.

n = int(input("Informe um número: "))
print("1 para binário")
print("2 para octal")
print("3 para hexadecimal")

while True:
    conv = (input("Quer converter para? "))
    if conv == "1":
        print(format(n, "b"))
        break
    elif conv == "2":
        print(format(n, "o"))
        break
    elif conv == "3":
        print(format(n, "x"))
        break
    else:
        print("Escolha invalida...")
        continue
