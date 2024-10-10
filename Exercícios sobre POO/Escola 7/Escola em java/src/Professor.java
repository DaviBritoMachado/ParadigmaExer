import java.util.ArrayList;

public class Professor {
    private String nome;
    private ArrayList<Escolas> contratos = new ArrayList<>();
    public Professor(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return this.nome;
    }

    public void contrato(Escolas escola){
        this.contratos.add(escola);
    }

    public void imprimir_contratos(){
        System.out.println(this.nome + " tem contratos com ");
        for(Escolas parceiro : contratos){
            System.out.println(parceiro.getNome());
        }
    }
}
