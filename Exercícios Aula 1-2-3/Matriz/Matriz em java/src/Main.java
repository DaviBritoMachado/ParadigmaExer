// Programa python para gerar automaticamente numeros
// entre 0 e 99 de uma cartela de bingo. Sabendo que cada
// cartela deverá ser 5x5, gere estes dados de modo a nao
// ter numeros repetidos dentro da cartela
// Davi Brito Machado
// RGM: 30116104

import java.util.HashSet;
import java.util.Iterator;
import java.util.Random;

public class Main {
    public static HashSet<Integer> gerar_cartela() {
        HashSet<Integer> cart = new HashSet<Integer>();

        while(cart.size() < 25){
            Random rand = new Random();
            int numero = rand.nextInt(99);
            cart.add(numero);
        }
        return cart;
    }

    public static void imprimir_cartela(HashSet<Integer> cartela){
        System.out.println("Cartela de bingo: ");
        Iterator<Integer> iterator = cartela.iterator();
        for (int i = 0; i < 5; i++){
            for (int j = 0; j < 5; j++){
                System.out.print(iterator.next() + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        HashSet<Integer> cartela = gerar_cartela();
        imprimir_cartela(cartela);
    }
}