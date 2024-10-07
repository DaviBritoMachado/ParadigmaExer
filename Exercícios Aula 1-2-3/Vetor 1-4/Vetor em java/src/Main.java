import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> vetorA = Func.faz_lista(8);

        Func.soma(vetorA.get(Func.leitura()), vetorA.get(Func.leitura()));

        Func.maior_menor(vetorA);

        Func.soma_lista(vetorA);

        ArrayList<Integer> vetorB = Func.faz_lista_aleatoria(8);

        ArrayList<Integer> vetorC = Func.soma_listas(vetorA, vetorB);

        Func.exibicao(vetorC);

        Func.par_impar_lista(vetorA);
    }
}