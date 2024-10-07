from imprimivel import Imprimivel

class Relatorio(Imprimivel):
    def __init__(self, texto) -> None:
        self.texto = texto

    def imprimir(self):
        print("Relatorio: " + self.texto)