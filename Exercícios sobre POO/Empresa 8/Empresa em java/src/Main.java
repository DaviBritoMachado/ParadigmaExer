/* 8. Agregação Modele uma classe Empresa que agregue uma lista de objetos Empregado.
   Cada empregado deve ter atributos como nome e cargo*/

public class Main {
    public static void main(String[] args) {
        Endereco endereco1 = new Endereco("Av. Principal", "Patapingas", "Minas Gerais", "12345-234");
        Funcionario pessoa1 = new Funcionario("João", "Faxineiro", "R$1500,00");
        pessoa1.adicionar_endereco(endereco1);
        pessoa1.mostrar_informacoes();

        Endereco endereco2 = new Endereco("Av. Secundaria", "Maraja", "Sao paulo", "54321-234");
        Funcionario pessoa2 = new Funcionario("Maria", "Gerente", "R$18000,00");
        pessoa2.adicionar_endereco(endereco2);

        Empresa empresa = new Empresa("Empresa ABC", "18509274");
        empresa.contratar_funcionarios(pessoa1);
        empresa.contratar_funcionarios(pessoa2);

        empresa.listar_funcionarios();
    }
}