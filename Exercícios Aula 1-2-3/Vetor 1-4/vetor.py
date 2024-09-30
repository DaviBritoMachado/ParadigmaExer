# Davi Brito Machado
# RGM: 30116104 

from func import *

def main():
    vetorA = fazListaAleatoria(8)

    soma(vetorA[leitura()], vetorA[leitura()])

    maiorEMenor(vetorA)
    
    somaLista(vetorA)

    vetorB = fazListaAleatoria(8)

    vetorC = somaListas(vetorA, vetorB)

    exibicao(vetorC)

    parLista(vetorA)

if __name__ == "__main__":
    main()