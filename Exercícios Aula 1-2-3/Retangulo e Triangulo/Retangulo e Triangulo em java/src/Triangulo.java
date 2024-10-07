public class Triangulo {
    private double lado1;
    private double lado2;
    private double lado3;

    public void set_lados(double l1, double l2, double l3){
        lado1 = l1;
        lado2 = l2;
        lado3 = l3;
    }

    public String tipo(){
        if(lado1 == lado2 & lado1 == lado3){
            return "Equilatero";
        }else if(lado1 == lado2 || lado1 == lado3 || lado2 == lado3){
            return "Isóceles";
        }else{
            return "Escaleno";
        }
    }

    public double calcular_perimetro(){
        return lado1 + lado2 + lado3;
    }
}

