/* 9. Interfaces/Protocolos Em Java e Golang, defina uma interface para imprimível que
   tenha um método imprimir. Implemente essa interface em classes como Relatório e
   Contrato.*/

public class Main {
    public static void main(String[] args) {
        Relatorio rela = new Relatorio();
        rela.set_texto("As vendas diminuiram em 74%, estamos em falencia");
        rela.imprimir();

        Contrato cont = new Contrato();
        cont.set_texto("Nosso contrato com o governo está acabando e eles não querem renovar");
        cont.imprimir();
    }
}