class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
    
    def __add__(self, other):
        preco = round(self.preco + other.preco, 2)
        return f"R${preco}"
    
