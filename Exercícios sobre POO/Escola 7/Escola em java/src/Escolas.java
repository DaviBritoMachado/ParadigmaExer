import java.util.ArrayList;

public class Escolas {
    private String nome;
    private ArrayList<Professor> contratos = new ArrayList<>();
    public Escolas(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return this.nome;
    }

    public void contrato(Professor professor){
        this.contratos.add(professor);
    }

    public void imprimir_contratos(){
        System.out.println(this.nome + " tem contrato com ");
        for(Professor parceiro : contratos){
            System.out.println(parceiro.getNome());
        }
    }
}
