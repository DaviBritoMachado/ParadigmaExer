// Davi Brito Machado
// 30116104
public class Main {
    public static void main(String[] args) {

        Retangulo ret = new Retangulo();
        ret.set_comprimento(200);
        ret.set_largura(100);
        System.out.println("Area: " + ret.calcular_area());
        System.out.println("Perimetro: " + ret.calcular_perimetro());

        Triangulo tri = new Triangulo();
        tri.set_lados(10, 30, 10);
        System.out.println("Tipo: " + tri.tipo());
        System.out.println("Perimetro: " + tri.calcular_perimetro());
    }
}