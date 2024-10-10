import static java.lang.Math.round;

public class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }

    public double add(Produto other){
        return round(this.preco + other.preco);
    }
}
