# 8. Agregação Modele uma classe Empresa que agregue uma lista de objetos Empregado.
# Cada empregado deve ter atributos como nome, cargo, e sala

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
            print("Endereco: ", end="")
            self.endereco.mostrar_endereco()
        else:
            print("Endereco não disponivel")

class Endereco:
    def __init__(self, rua, cidade, estado, cep) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
    
    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

class Empresa:
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        print(f"Funcionarios da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

def main():
    endereco1 = Endereco("Av. Principal", "Patapingas", "Minas Gerais", "12345-234")
    pessoa1 = Funcionario("João", "Faxineiro", "R$1500,00")
    pessoa1.adicionar_endereco(endereco1)
    pessoa1.mostrar_informacoes()

    endereco2 = Endereco("Av. Secundaria", "Maraja", "Sao paulo", "54321-234")
    pessoa2 = Funcionario("Maria", "Gerente", "R$18000,00")
    pessoa2.adicionar_endereco(endereco2)

    empresa = Empresa("Empresa ABC", "18509274")
    empresa.contratar_funcionarios(pessoa1)
    empresa.contratar_funcionarios(pessoa2)

    empresa.listar_funcionarios()

if __name__ == "__main__":
    main()