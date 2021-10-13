from pessoa import Pessoa

class Casamento(Pessoa):
    def __init__(self, cpf, nome, telefone, idade, padre):
        
        super().__init__(cpf, nome, telefone, idade, padre)

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

