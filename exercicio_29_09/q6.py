# Desenvolve um programa que solicite a quantidade de dias que o veículo foi alugado e a quantidade kilometros percorridos. Sabendo que o veículo custa R$58 a diária e R$0,21 por km rodado, calcule o total gasto

dias = int(input("Quantos dias o carro está alugado? "))
km = int(input("Quantos kilometros o carro rodou? "))

dias = dias * 58
km = km * 0.21
total = dias + km

print(f"O total gasto foi igual a R$ {total:.2f}")