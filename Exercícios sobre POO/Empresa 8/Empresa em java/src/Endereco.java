public class Endereco {
    private String rua;
    private String cidade;
    private String estado;
    private String cep;

    public Endereco(String rua, String cidade, String estado, String cep){
        this.rua = rua;
        this.cidade = cidade;
        this.estado = estado;
        this.cep = cep;
    }

    public void mostrar_endereco(){
        System.out.println("Endereco: Rua: " + this.rua + ", Cidade: " +
                this.cidade + ", Estado: " + this.estado + ", CEP: " + this.cep);
    }
}
