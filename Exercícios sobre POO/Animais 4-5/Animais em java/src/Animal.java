import java.util.ArrayList;

public class Animal {
    private String especie;
    private String nome;

    public Animal(String especie, String nome){
        this.especie = especie;
        this.nome = nome;
    }

    public String emitir_som(){
        return "som de animal";
    }

    public static void som_todos_animais(ArrayList<Animal> lista){
        for(Animal animal : lista){
            System.out.println(animal.emitir_som());
        }
    }
}
