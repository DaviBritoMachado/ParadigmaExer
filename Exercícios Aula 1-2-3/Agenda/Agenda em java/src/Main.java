// Coletar os dados do usuário: Recebe uma lista de nomes e idades
// Armazena dados em um dicionario e usa para associar cada nome
// a sua idade
// Salva arquivos em .txt
// Davi Brito Machado
// RGM: 30116104

import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Main {
    public static ArrayList<HashMap> coletar_dados(){
        ArrayList<HashMap> dados = new ArrayList<>();
        while(true){
            Scanner scan = new Scanner(System.in);
            System.out.println("Digite o nome(ou 'sair' para encerrar): ");
            String nome = scan.nextLine();
            if(Objects.equals(nome.toLowerCase(), "sair")){
                break;
            }
            HashMap<String, String> stri_hash = new HashMap<>();
            stri_hash.put("Nome", nome);
            System.out.println("Digite a idade: ");
            String idade = scan.nextLine();
            stri_hash.put("Idade", idade);
            System.out.println("Digite o telefone: ");
            String telefone = scan.nextLine();
            stri_hash.put("Telefone", telefone);
            dados.add(stri_hash);
        }
        return dados;
    }

    public static void salvar_em_arquivos(ArrayList<HashMap> dados,String nome_Arquivo) {
        try {
            FileWriter escrito = new FileWriter(nome_Arquivo);
            for(HashMap item : dados){
                String linha = "Nome: " + item.get("Nome") + ", Idade: " + item.get("Idade") + ", Telefone: " + item.get("Telefone");
                escrito.write(linha);
            }
            escrito.close();
            System.out.println("Dados salvos no arquivo " + nome_Arquivo);
        }catch (IOException e) {
            System.out.println("Erro");
        }
    }

    public static void main(String[] args) {
        ArrayList<HashMap> dados = new ArrayList<>();
        dados = coletar_dados();
        if(!dados.isEmpty()){
            salvar_em_arquivos(dados, "dadosPessoas.txt");
        }else{
            System.out.println("Nenhum dado foi coletado");
        }
    }
}