/* 1. Classes e Objetos Básicos Crie uma classe Carro com atributos como marca, modelo, e
   ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.
   2. Métodos Adicione um método acelerar e frear à classe Carro que altere um atributo
   velocidade. Crie um método para exibir a velocidade atual.
   6. Composição Implemente uma classe Motor e associe-a a uma classe Carro. A classe
   Carro deve ter um objeto do tipo Motor como um de seus atributos.*/

public class Main {
    public static void main(String[] args) {
        Carro carro = new Carro("Toyota", "Corolla");
        carro.ligar();
        carro.acelerar();
        carro.mostrar_velocidade();
        carro.frear();

        Pneu novo_pneu = new Pneu("Michelin", 17);
        carro.trocar_pneu(2, novo_pneu);

        carro.desligar();
    }
}