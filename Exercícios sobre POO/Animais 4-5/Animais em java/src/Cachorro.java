public class Cachorro extends Animal{
    public Cachorro(String especie, String nome) {
        super(especie, nome);
    }

    public String emitir_som(){
        return "au au";
    }
}
