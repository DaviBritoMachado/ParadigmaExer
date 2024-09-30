# 7. Associação Crie uma classe Escola e uma classe Professor. A associação deve permitir
# que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

class Escola:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.contratos = []

class Professor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.contratos = []

def contrato_escola_professor(escola, professor):
    escola.contratos.append(professor)
    professor.contratos.append(escola)

def imprimir_contratos(self):
        print(self.nome + " tem contrato com")
        for parceiro in self.contratos:
            print(parceiro.nome)

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
