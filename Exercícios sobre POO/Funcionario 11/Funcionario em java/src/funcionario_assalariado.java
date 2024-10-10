public class funcionario_assalariado extends funcionario_abs {
    public funcionario_assalariado(String nome, String cargo){
        this.nome = nome;
        this.cargo = cargo;
    }
    public double calcular_salario(double preco_hora, double dias){
        return preco_hora * 8 * dias;
    }
}
