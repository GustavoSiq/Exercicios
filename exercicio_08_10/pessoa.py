class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
    
    # Getters e Setters
    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone

    # Metodos
    def entrar(self):
        print("Já vai começar, vamos entrar!")

    def sentar(self):
        print("Cansei de esperar, vou sentar!")
    
    def sair(self, fim):
        print("Terminou? ")
        if fim == 'sim':
            print("Foi lindo, mas terminou, vamos embora!")
        