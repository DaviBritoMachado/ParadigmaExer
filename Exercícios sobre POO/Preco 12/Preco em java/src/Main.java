/* 12. Sobrecarga de Operadores (Python) / Métodos de Conveniência (Java, Go) Em Python,
   sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
   e Golang, crie métodos que permitam essa funcionalidade.*/

public class Main {
    public static void main(String[] args) {
        Produto prod1 = new Produto("maça", 2.01);
        Produto prod2 = new Produto("banana", 1.55);

        System.out.println(prod1.add(prod2));
    }
}