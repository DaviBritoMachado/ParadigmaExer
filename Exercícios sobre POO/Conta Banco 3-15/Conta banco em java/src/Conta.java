public class Conta {
    private String titular;
    private double saldo;

    public Conta(String titular, double saldo){
        this.titular = titular;
        this.saldo = saldo;
    }

    public void sacar(double valor){
        try{
            if(this.saldo > valor){
                this.saldo -= valor;
                System.out.println("Voce sacou R$" + valor + "ficando com um saldo de R$" + this.saldo);
            }else{
                throw new SaldoInsuficienteException();
            }
        }catch(SaldoInsuficienteException ex){
            System.err.print(ex);
        }
    }
}
