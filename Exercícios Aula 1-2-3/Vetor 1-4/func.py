import random

def fazLista(x):
    vetor = [0] * x

    for i in range(x):
        vetor[i] = int(input("Digite o valor da posicao {}: ".format(i)))

    return vetor

def fazListaAleatoria(x):
    vetor = []

    for i in range(x):
        vetor.append(int(random.uniform(0, 100)))

    return vetor

def somaListas(vetorA, vetorB):
    vetorC = []

    for i in range(len(vetorA)):
        vetorC.append(vetorA[i] + vetorB[i])

    return vetorC

def leitura():
    return int(input("Digite a posicao desejada: "))

def exibicao(vetor):
    for i in range(len(vetor)):
        print(vetor[i], " ", end=" ")
    print("")

def soma(x, y):
    return print(x + y)

def maiorEMenor(vetor):
    maior = 0
    menor = 99999

    for i in range(0, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]
    return print("Maior elemento é ", maior ," e menor elemento e", menor)

def somaLista(vetor):
    soma = 0

    for i in range(0, len(vetor)):
        soma += vetor[i]
    return print("Soma e %d" % soma)

#  Esta função exibirá
#  • Os números pares digitados; 
#  • A soma dos numeros pares digitados; 
#  • Os números ímpares digitados;
#  • A quantidade de números ímpares
def parLista(vetor):
    numerosPares = []
    numerosImpares = []
    somaPares = 0

    for numero in vetor:
        if numero % 2 == 0:
            numerosPares.append(numero)
            somaPares += numero
        else:
            numerosImpares.append(numero)
    
    print("Os números pares digitados são: ", end="")
    for numero in numerosPares:
        print(numero, " ", end="")

    print("\nA soma dos números pares digitados é:", somaPares,)

    print("Os números ímpares digitados são: ", end="")
    for numero in numerosImpares:
        print(numero, " ", end="")

    print("\nA quantidade de números ímpares digitados é:", len(numerosImpares))