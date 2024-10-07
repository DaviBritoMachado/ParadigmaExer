public class Retangulo {
    private double comprimento;
    private double largura;

    public void set_comprimento(double comp){
        comprimento = comp;
    }

    public void set_largura(double larg){
        largura = larg;
    }

    public double calcular_area(){
        return comprimento * largura;
    }

    public double calcular_perimetro(){
        return 2 * (comprimento + largura);
    }
}