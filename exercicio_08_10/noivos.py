from pessoa import Pessoa

class Noivos(Pessoa):
    def __init__(self, cpf, nome, telefone, idade, padre):
        
        super().__init__(cpf, nome, telefone)

        self._idade = idade
        self._padre = padre

    # Getters e Setters
    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        self._idade = idade
    
    def get_padre(self):
        return self._padre

    def set_padre(self, padre):
        self._padre = padre

    # Metodos
    def subirAltar(self):
        print("Bora? Tá na hora!")

    def colocarAnel(self, confirmacao):
        print(f"{self._nome}: {confirmacao}")
        if confirmacao == 'sim':
            print("Mê de a mão...")
        else:
            print("Vish, deu ruim!")
    
    def beijar(self):
        print("Os noivos podem se beijar!")