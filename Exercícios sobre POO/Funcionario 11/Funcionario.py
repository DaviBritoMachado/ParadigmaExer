# 11. Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
# calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
# implementam calcularSalario de formas distintas.

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cargo) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = None
    
    @abstractmethod
    def calcular_salario(self):
        pass

class Funcionario_horista(Funcionario):
    def calcular_salario(self, preco_hora, hora_dia, dias):
        return preco_hora * hora_dia * dias
    
class Funcionario_assalariado(Funcionario):
    def calcular_salario(self, preco_hora, dias):
        return preco_hora * 8 * dias
    
def main():
    funci1 = Funcionario_assalariado("Jorge", "Professor")
    funci2 = Funcionario_horista("Pereira", "Faz-tudo")

    print(funci1.calcular_salario(50, 20))
    print(funci2.calcular_salario(70, 4, 4))

if __name__ == "__main__":
    main()