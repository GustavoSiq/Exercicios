# Faça um programa que leia a velocidade de vários veículos. Se ultrapassar 80 Km/h, reporte a mensagem informando que foi multado. O valor da multa é R$ 45,00 por cada Km acima do limite. Para sair do programa, será necessário digitar sair.

while True:
    n = int(input("Informe a velocidade: "))
    if n == 80:
        print(f"Você foi multado! Multa: R$ 45,00")
    elif n > 80:
        n = (n - 80) * 45
        print(f"Você foi multado! Multa R$ {n:.2f}")
    elif n < 80 :
        continue
    elif "sair":
        break
