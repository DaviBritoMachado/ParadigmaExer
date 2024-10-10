public class Contrato{
    public void contrato_escola_professor(Escolas escola, Professor professor){
        escola.contrato(professor);
        professor.contrato(escola);
    }
}
