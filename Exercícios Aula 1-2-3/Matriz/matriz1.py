# Programa python para gerar automaticamente numeros
# entre 0 e 99 de uma cartela de bingo. Sabendo que cada
# cartela deverá ser 5x5, gere estes dados de modo a nao 
# ter numeros repetidos dentro da cartela
# Davi Brito Machado
# RGM: 30116104 

import random

def gerar_cartela():
    cart = set()

    while len(cart) < 25:
            numero = random.randint(0, 99)
            cart.add(numero)
    return cart

def imprimir_cartela(cartela):
    print("Cartela de bingo: ")
    for i in range(5):
        for j in range(5):
            print(cartela.pop(), " ", end="")
        print("")

def main():
    cartela = gerar_cartela()
    imprimir_cartela(cartela)
    

if __name__ == "__main__":
    main()