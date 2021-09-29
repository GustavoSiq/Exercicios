# Todo ano há reajuste salário e a tabela do próximo ano está na tabela abaixo. Faça um programa que calcule o reajuste do funcionário de acordo com o salário atual.
# Salário atual	Reajuste
# Abaixo de R$ 700	12%
# de R$ 700 até R$1200	10%
# Acima de R$1200	5%

salario = float(input("Informe o salário: "))
reajueste = 0

if salario < 700:
    reajueste = salario * 1.12
elif salario >= 700 and salario <= 1200:
    reajueste = salario * 1.10
else:
    reajueste = salario * 1.05

print(f"O novo salário vai ser R$ {reajueste:.2f}")