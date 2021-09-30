# Sabendo que o dólar comercial está a ( R$ 5,49 ) na cotação do dia Faça um programa que leia o dinheiro que possui na carteira em ( R$ Real ) e converta para ( $ Dólar )

n = float(input("Informe um valor: "))

n = n / 5.49

print(f"O valor informado em Dólar fica igual a R$ {n:.2f}")