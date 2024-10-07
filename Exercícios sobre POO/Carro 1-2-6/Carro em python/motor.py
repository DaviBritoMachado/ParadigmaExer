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