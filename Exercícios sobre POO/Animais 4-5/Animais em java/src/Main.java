/* 4. Herança Crie uma classe base Animal com métodos como som. Derive classes como
   Cachorro e Gato que implementam o método som de maneiras diferentes.
   5. Polimorfismo Utilize polimorfismo para criar uma função que receba uma lista de
   objetos Animal e chame o método som de cada um, demonstrando comportamento
   diferente para cada subclasse.*/

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Cachorro cachorro = new Cachorro("Buldog", "Tobi");
        Gato gato = new Gato("Laranja", "Morte");
        Galinha galinha = new Galinha("Branca", "Gala");

        ArrayList<Animal> lista = new ArrayList<>();
        lista.add(cachorro);
        lista.add(gato);
        lista.add(galinha);
        Animal.som_todos_animais(lista);
    }
}