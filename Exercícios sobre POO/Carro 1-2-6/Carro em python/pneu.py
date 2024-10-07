class Pneu:
    def __init__(self, marca, tamanho) -> None:
        self.marca = marca
        self.tamanho = tamanho

    def inflar(self):
        print("O pneu esta inflado")

    def desinflar(self):
        print("O pneu esta desinflado")