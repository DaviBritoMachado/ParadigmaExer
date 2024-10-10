class Matematica:
    def __init__(self) -> None:
        pass

    @staticmethod
    def fatorial(numero):
        fator = 1
        while numero > 0:
            fator *= numero
            numero -= 1
        return fator