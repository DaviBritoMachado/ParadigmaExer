import java.util.ArrayList;

public class Empresa {
    private String nome;
    private String cnpj;
    private ArrayList<String> funcionarios = new ArrayList<>();

    public Empresa(String nome, String cnpj){
        this.nome = nome;
        this.cnpj = cnpj;
    }

    public void contratar_funcionarios(Funcionario funcionario){
        this.funcionarios.add(funcionario.getNome());
    }

    public void listar_funcionarios(){
        System.out.println("Funcionarios da empresa " + this.nome + ":");
        for(String funcionario : funcionarios){
            System.out.println(funcionario);
        }
    }
}
