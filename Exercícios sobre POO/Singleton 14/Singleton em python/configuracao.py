from singleto import Singleton

class Configuracao:
    __metaclass__ = Singleton

    def __init__(self) -> None:
        self.ligado = False

    def ligar(self):
        self.ligado = True