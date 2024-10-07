from imprimivel import Imprimivel

class Contrato(Imprimivel):
    def __init__(self, texto) -> None:
        self.texto = texto

    def imprimir(self):
        print("Contrato: " + self.texto)