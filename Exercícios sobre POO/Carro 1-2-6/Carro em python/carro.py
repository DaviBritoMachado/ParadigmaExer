from motor import Motor
from pneu import Pneu

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = Motor("Gasolina", 150) # Composição
        self.pneus = [Pneu("Pirelli", 18) for _ in range(4)] # Composição
        self.velocidade = 0

    def detalhes(self):
        print(f'Marca {self.marca}, modelo {self.modelo} e ano {self.ano}')

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