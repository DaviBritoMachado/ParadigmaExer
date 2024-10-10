class Funcionario:
    def __init__(self, nome, cargo, salario) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = None

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salario: {self.salario}")
        if self.endereco:
            self.endereco.mostrar_endereco()
        else:
            print("Endereco não disponivel")