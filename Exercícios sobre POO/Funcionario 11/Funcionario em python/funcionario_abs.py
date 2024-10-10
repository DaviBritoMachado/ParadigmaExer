from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cargo) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = None
    
    @abstractmethod
    def calcular_salario(self):
        pass