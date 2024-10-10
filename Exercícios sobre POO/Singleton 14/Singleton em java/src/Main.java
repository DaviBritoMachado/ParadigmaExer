public class Main {
    public static void main(String[] args) {
        Configuracao confi = Configuracao.get_instancia();
        confi.ligar();
        Configuracao confi2 = Configuracao.get_instancia();

        System.out.println(confi.get_ligado());
        System.out.println(confi2.get_ligado());
    }
}