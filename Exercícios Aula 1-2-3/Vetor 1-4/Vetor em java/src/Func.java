import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
public class Func {
    public static ArrayList<Integer> faz_lista(int x){
        ArrayList<Integer> vetor = new ArrayList<>();
        Scanner scan = new Scanner(System.in);

        for(int i = 0; i < x; i++){
            System.out.println("Digite o valor da posição " + i + ": ");
            vetor.add(scan.nextInt());
        }
        return vetor;
    }
    public static ArrayList<Integer> faz_lista_aleatoria(int x){
        ArrayList<Integer> vetor = new ArrayList<>();
        Random rand = new Random();

        for(int i = 0; i < x; i++){
            vetor.add(rand.nextInt(0, 100));
        }
        return vetor;
    }
    public static ArrayList<Integer> soma_listas(ArrayList<Integer> vetorA, ArrayList<Integer> vetorB){
        ArrayList<Integer> vetorC = new ArrayList<>();

        for(int i = 0; i < vetorA.size(); i++){
            vetorC.add(vetorA.get(i) + vetorB.get(i));
        }

        return vetorC;
    }
    public static int leitura(){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o valor da posição desejada: ");
        return(scan.nextInt());
    }

    public static void exibicao(ArrayList<Integer> vetor){
        for(int i = 0; i < vetor.size(); i++){
            System.out.print(vetor.get(i) + " ");

        }
        System.out.println();
    }
    public static void soma(int x, int y){
        System.out.println(x + y);
    }
    public static void maior_menor(ArrayList<Integer> vetor){
        int maior = 0;
        int menor = 9999;

        for(int i = 0; i < vetor.size(); i++){
            if(vetor.get(i) > maior){
                maior = vetor.get(i);
            }
            if(vetor.get(i) < menor){
                menor = vetor.get(i);
            }
        }
        System.out.println("Maior elemento é " + maior + " e o menor é " + menor);
    }
    public static void soma_lista(ArrayList<Integer> vetor){
        int soma = 0;
        for(int i : vetor){
            soma += i;
        }
        System.out.println("Soma dos valores é " + soma);
    }
    /*  Esta função exibirá
        • Os números pares digitados;
        • A soma dos numeros pares digitados;
        • Os números ímpares digitados;
        • A quantidade de números ímpares */
    public static void par_impar_lista(ArrayList<Integer> vetor){
        ArrayList<Integer> pares = new ArrayList<>();
        ArrayList<Integer> impares = new ArrayList<>();
        int soma_pares = 0;

        for(int i : vetor){
            if(i % 2 == 0){
                pares.add(i);
                soma_pares += i;
            }else{
                impares.add(i);
            }
        }

        System.out.print("Os números pares digitatos são: ");
        for(int i : pares){
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println("A soma dos números pares é: " + soma_pares);

        System.out.print("Os números ímpares digitatos são: ");
        for(int i : impares){
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println("A quantidade de números ímpares digitados é: " + impares.size());
    }
}
