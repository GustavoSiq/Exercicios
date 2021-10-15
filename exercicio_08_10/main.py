from casamento import Casamento
from noivos import Noivos
from pessoa import Pessoa

casamento = Casamento('Rua dos bobos', 0, 32)
noivos = Noivos(1111111111, 'Rafael', 88889999, 42, 'Pe. Zezin')
pessoa = Pessoa(0000000000, 'Gustavo', 40028922)

# casamento
casamento.Buquê()
casamento.Bolo()
resultado = input(f"Você aceita se casar? ")
casamento.casados(resultado)

# noivos
noivos.subirAltar()
confirmacao = input(f"Você aceita se casa com sua noiva? ")
noivos.colocarAnel(confirmacao)
noivos.beijar()

# pessoa
pessoa.entrar()
pessoa.sentar()
while True:
    fim = input(f"Terminou? ")
    if fim == 'sim':
        break
    else:
        print(":/")
        continue
pessoa.sair(fim)