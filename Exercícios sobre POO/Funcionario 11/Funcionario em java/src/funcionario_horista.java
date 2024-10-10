public class funcionario_horista extends funcionario_abs {
    public funcionario_horista(String nome, String cargo){
        this.nome = nome;
        this.cargo = cargo;
    }

    public double calcular_salario(double preco_hora, double hora_dia, double dias){
        return preco_hora * hora_dia * dias;
    }
}
