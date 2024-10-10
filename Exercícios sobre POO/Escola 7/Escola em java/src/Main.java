/* 7. Associação Crie uma classe Escola e uma classe Professor. A associação deve permitir
   que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.*/

public class Main {
    public static void main(String[] args) {
        Escolas escola1 = new Escolas("Ensino");
        Escolas escola2 = new Escolas("Felicidade");

        Professor prof1 = new Professor("Jorge");
        Professor prof2 = new Professor("Iranildo");

        Contrato contrato = new Contrato();
        contrato.contrato_escola_professor(escola1, prof1);
        contrato.contrato_escola_professor(escola2, prof1);
        contrato.contrato_escola_professor(escola1, prof2);

        prof1.imprimir_contratos();
        escola1.imprimir_contratos();
    }
}