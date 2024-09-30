# 12. Sobrecarga de Operadores (Python) / Métodos de Conveniência (Java, Go) Em Python,
# sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
# e Golang, crie métodos que permitam essa funcionalidade.

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
    
    def __add__(self, other):
        preco = round(self.preco + other.preco, 2)
        return f"R${preco}"
    
def main():
    prod1 = Produto("maça", 2.01)
    prod2 = Produto("banana", 1.55)

    print(prod1 + prod2)

if __name__ == "__main__":
    main()