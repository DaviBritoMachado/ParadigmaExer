# Davi Brito Machado
# 30116104
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return (self.lado1 + self.lado2 + self.lado3)
    
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    
def main():
    ret = Retangulo(200, 100)
    print("Area: ",  ret.calcular_area())
    print("Perimetro: ", ret.calcular_perimetro())

    tri = Triangulo(10, 30, 10)
    print("Perimetro: ", tri.calcular_perimetro())
    print("Tipo: " + tri.tipo())

if __name__ == "__main__":
    main()
    