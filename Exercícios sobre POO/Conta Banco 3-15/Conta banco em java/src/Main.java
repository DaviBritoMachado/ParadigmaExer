/* 3. Encapsulamento Implemente uma classe ContaBancaria com atributos saldo, titular e
   métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.
   15. Exceções/Erros Personalizados Crie uma classe de exceção personalizada
   SaldoInsuficienteException que seja lançada quando houver uma tentativa de saque
   superior ao saldo disponível na classe ContaBancaria*/

public class Main {
    public static void main(String[] args) throws SaldoInsuficienteException {
        Conta conta = new Conta("Jorge", 200);
        conta.sacar(550.37);
    }
}