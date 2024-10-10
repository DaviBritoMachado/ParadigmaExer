public class Funcionario {
    private String nome;
    private String cargo;
    private String salario;
    private Endereco endereco;

    public Funcionario(String nome, String cargo, String salario){
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    public String getNome(){
        return this.nome;
    }

    public void adicionar_endereco(Endereco endereco){
        this.endereco = endereco;
    }

    public void mostrar_informacoes(){
        System.out.println("Nome: " + this.nome + ", Cargo: " + this.cargo + ", Salario: " + this.salario);
        if(this.endereco != null){
            this.endereco.mostrar_endereco();
        }else{
            System.out.println("Endereço não disponivel");
        }
    }
}
