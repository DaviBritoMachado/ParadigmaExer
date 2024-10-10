# 8. Agregação Modele uma classe Empresa que agregue uma lista de objetos Empregado.
# Cada empregado deve ter atributos como nome e cargo

from funcionario import Funcionario
from endereco import Endereco
from empresa import Empresa

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