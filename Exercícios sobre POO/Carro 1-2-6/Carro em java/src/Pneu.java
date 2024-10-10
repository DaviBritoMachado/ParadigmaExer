public class Pneu {
    private String marca;
    private double tamanho;
    public Pneu(String marca, int tamanho) {
        this.marca = marca;
        this.tamanho = tamanho;
    }
    public void inflar(){
        System.out.println("O pneu esta inflado");
    }
    public void desinflar(){
        System.out.println("O pneu esta desinflado");
    }
}