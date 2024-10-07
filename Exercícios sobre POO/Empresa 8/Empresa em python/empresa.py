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