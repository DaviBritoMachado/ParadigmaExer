# 10. Sobrecarga de Métodos (Java) / Métodos com Nomes Diferentes (Python, Go)
# Implemente uma classe Calculadora com métodos somar que aceita diferentes números
# de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
# para diferentes quantidades de parâmetros.
# 13. Métodos Estáticos Adicione um método estático à classe Matematica que calcula o
# fatorial de um número. Em Python, utilize @staticmethod, em Java static, e em Golang crie
# uma função regular na struct.

class Calculadora:
    def __init__(self) -> None:
        pass

    def soma(self, x, y):
        return x + y
    
    def soma3(self, x, y ,z):
        return x + y + z
    
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

def main():
    calc = Calculadora()
    print(calc.soma(1, 2))
    print(calc.soma3(1, 2, 3))

    mat = Matematica()
    print(mat.fatorial(4))

if __name__ == "__main__":
    main()