# 9. Interfaces/Protocolos Em Java e Golang, defina uma interface para imprimível que
# tenha um método imprimir. Implemente essa interface em classes como Relatório e
# Contrato. Em Python, use a abordagem de protocolo ou classes abstratas.

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Relatorio(Imprimivel):
    def __init__(self, texto) -> None:
        self.texto = texto

    def imprimir(self):
        print("Relatorio: " + self.texto)

class Contrato(Imprimivel):
    def __init__(self, texto) -> None:
        self.texto = texto

    def imprimir(self):
        print("Contrato: " + self.texto)

def main():
    relatorio = Relatorio("As vendas diminuiram em 74%, estamos em falencia")
    relatorio.imprimir()

    contrato = Contrato("Nosso contrato com o governo está acabando e eles não querem renovar")
    contrato.imprimir()
if __name__ == "__main__":
    main()