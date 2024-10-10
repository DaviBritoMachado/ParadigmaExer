public class Configuracao {
    private static Configuracao instancia;
    private boolean ligado;

    private Configuracao() {
        this.ligado = false;
    }

    public static synchronized Configuracao get_instancia() {
        if (instancia == null) {
            instancia = new Configuracao();
        }
        return instancia;
    }

    public void ligar() {
        this.ligado = true;
    }

    public boolean get_ligado() {
        return this.ligado;
    }
}