# Coletar os dados do usuário: Recebe uma lista de nomes e idades
# Armazena dados em um dicionario e usa para associar cada nome
# a sua idade
# Salva arquivos em .txt
# Davi Brito Machado
# RGM: 30116104 
def coletarDados():
    dados = []
    while True:
        nome = input("Digite o nome(ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um numero inteiro")
            continue
        telefone = input("Digite o telefone: ")

        dados.append({'nome' : nome, 'idade': idade, 'telefone': telefone})
    return dados

def salvarEmArquivos(dados, nomeArquivo):
    with open(nomeArquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}, Telefone: {item['telefone']}\n"
            arquivo.write(linha)

def main():
    dados = coletarDados()
    if dados:
        salvarEmArquivos(dados, 'dadosPessoas.txt')
        print("Dados salvos no arquivo dadosPessoas.txt")
    else:
        print("Nenhum dado foi coletado")

if __name__ == "__main__":
    main()