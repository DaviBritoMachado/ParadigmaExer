public class Motor {
    private String tipo;
    private double potencia;
    private boolean ligado;

    public Motor(String tipo, int potencia) {
        this.tipo = tipo;
        this.potencia = potencia;
    }

    public boolean get_ligado(){
        return this.ligado;
    }

    public void ligar(){
        this.ligado = true;
        System.out.println("O motor está ligado");
    }
    public void desligar(){
        this.ligado = false;
        System.out.println("O motor está desligado");
    }
}