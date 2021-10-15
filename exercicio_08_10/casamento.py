class Casamento:
    def __init__(self, rua, numero, dia):
        self._rua = rua
        self._numero = numero
        self._dia = dia

    # Getters e Setters
    def get_rua(self):
        return self._rua

    def set_rua(self, rua):
        self._rua = rua

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_dia(self):
        return self._dia

    def set_dia(self, dia):
        self._dia = dia

    # Metodos
    def Bolo(self):
        print("E o primeiro pedaço vai para...")

    def casados(self, resposta):
        if resposta == 'sim':
            print("Finalmente se casaram!!")
        else:
            print("Vish, deu ruim!")
    
    def Buquê(self):
        print("Eu vou jogar...")