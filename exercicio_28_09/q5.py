# Usando o nome dos seus colegas Aline, Bruna, Gustavo, Huan, Marlon, Rafa, Rafael e Victor, faça um programa que leia os nomes e sortei um deles para responder a próxima questão, escrevendo na tela o nome do escolhido.

import random

lista = ["Aline", "Bruna", "Gustavo", "Huan", "Marlon", "Rafa", "Rafael", "Victor"]

print(f"O escolhido foi: {random.choice(lista)}")