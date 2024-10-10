public class Matematica {
    public static int fatorial(int numero){
        int fator = 1;
        while(numero > 0){
            fator *= numero;
            numero -= 1;
        }
        return fator;
    }
}
