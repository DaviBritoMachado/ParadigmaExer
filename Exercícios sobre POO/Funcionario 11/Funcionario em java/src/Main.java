public class Main {
    public static void main(String[] args) {
        funcionario_assalariado funci1 = new funcionario_assalariado("Jorge", "Professor");
        funcionario_horista funci2 = new funcionario_horista("Pereira", "Faz-tudo");

        System.out.println(funci1.calcular_salario(50, 20));
        System.out.println(funci2.calcular_salario(70, 4, 4));
    }
}