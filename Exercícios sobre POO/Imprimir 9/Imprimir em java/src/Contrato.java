public class Contrato implements Imprimivel{
    private String texto;
    public String get_texto() {
        return this.texto;
    }
    public void set_texto(String texto) {
        this.texto = texto;
    }
    @Override
    public void imprimir() {
        System.out.println("Contrato: " + this.texto);
    }
}

