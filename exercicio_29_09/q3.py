# Desenvolve um programa que leia um número com até 4 casas decimais e que retorne informando qual é o número de cada casa decimal.
# Exemplo: 1258
# Milhar: 1
# Centena: 2
# Dezena: 5
# Unidade: 8

n = int(input("Informe um número: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(m)
print(c)
print(d)
print(u)