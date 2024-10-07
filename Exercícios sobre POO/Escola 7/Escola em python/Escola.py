# 7. Associação Crie uma classe Escola e uma classe Professor. A associação deve permitir
# que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

from escolas import Escola
from professor import Professor
from contrato import *

def main():
    escola1 = Escola("Ensino")
    escola2 = Escola("Felicidade")

    prof1 = Professor("Jorge")
    prof2 = Professor("Iranildo")

    contrato_escola_professor(escola1, prof1)
    contrato_escola_professor(escola2, prof1)
    contrato_escola_professor(escola1, prof2)

    imprimir_contratos(prof1)
    imprimir_contratos(escola1)


if __name__ == "__main__":
    main()
