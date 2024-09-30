# 1. Classes e Objetos Básicos Crie uma classe Carro com atributos como marca, modelo, e
# ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.
# 2. Métodos Adicione um método acelerar e frear à classe Carro que altere um atributo
# velocidade. Crie um método para exibir a velocidade atual.
# 6. Composição Implemente uma classe Motor e associe-a a uma classe Carro. A classe
# Carro deve ter um objeto do tipo Motor como um de seus atributos.

class Motor:
    def __init__(self, tipo, potencia) -> None:
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        print("O motor esta ligado")

    def desligar(self):
        self.ligado = False
        print("O motor esta desligado")

class Pneu:
    def __init__(self, marca, tamanho) -> None:
        self.marca = marca
        self.tamanho = tamanho

    def inflar(self):
        print("O pneu esta inflado")

    def desinflar(self):
        print("O pneu esta desinflado")

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.modelo = ano
        self.motor = Motor("Gasolina", 150) # Composição
        self.pneus = [Pneu("Pirelli", 18) for _ in range(4)] # Composição
        self.velocidade = 0

    def ligar(self):
        self.motor.ligar()
        print("O carro esta pronto para rodar")

    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado")

    def trocar_pneu(self, indice, novo_pneu):
        self.pneus[indice] = novo_pneu
        print(f"Pneu {indice + 1} trocado")

    def acelerar(self):
        if(self.motor.ligado):
            self.velocidade += 10
            print("O carro está acelerando")
        else:
            print("O carro esta desligado")

    def frear(self):
        if(self.motor.ligado):
            if(self.velocidade > 0):
                self.velocidade -= 10
                print("O carro está freando")
            else:
                print("O carro está parado")
        else:
            print("O carro esta desligado")

    def mostrar_velocidade(self):
        print(f"A velocidade do carro é de {self.velocidade} Km")

def main():
    carro = Carro("Toyota", "Corolla", 2000)
    carro.ligar()
    carro.acelerar()
    carro.mostrar_velocidade()
    carro.frear()

    novo_pneu = Pneu("Michelin", 17)
    carro.trocar_pneu(2, novo_pneu)
    carro.desligar()

if __name__ == "__main__":
    main()