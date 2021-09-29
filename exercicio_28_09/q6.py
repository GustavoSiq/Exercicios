# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

tuple = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = -1

while n < 0 or n > 10:
    n = int(input('Digite um número entre 0 e 10: '))

print(f'Você digitou o número {tuple[n]}')