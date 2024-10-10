import java.util.ArrayList;

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private Motor motor;
    private ArrayList<Pneu> pneus;
    private int velocidade;

    public Carro(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.motor = new Motor("Gasolina", 150);
        this.pneus = new ArrayList<Pneu>();
        for (int i = 0; i < 4; i++) {
            pneus.add(new Pneu("Pirelli", 18));
        }
    }

    public void ligar() {
        this.motor.ligar();
        System.out.println("O carro esta pronto para rodar");
    }

    public void desligar() {
        this.motor.desligar();
        System.out.println("O carro foi desligado");
    }

    public void trocar_pneu(int indice, Pneu novo_pneu){
        this.pneus.set(indice, novo_pneu);
        System.out.println("Pneu " + indice + " trocado");
    }

    public void acelerar(){
        if(this.motor.get_ligado()){
            this.velocidade += 10;
            System.out.println("O carro está acelerando");
        }else{
            System.out.println("O carro está desligado");
        }
    }

    public void frear(){
        if(this.motor.get_ligado()){
            if(this.velocidade > 0){
                this.velocidade -= 10;
                System.out.println("O carro está freando");
            }else{
                System.out.println("O carro esta parado");
            }

        }else{
            System.out.println("O carro está desligado");
        }
    }

    public void mostrar_velocidade(){
        System.out.println("A velocidade do carro é " + this.velocidade + " Km");
    }
}