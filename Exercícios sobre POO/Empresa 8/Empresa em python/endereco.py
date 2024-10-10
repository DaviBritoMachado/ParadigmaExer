class Endereco:
    def __init__(self, rua, cidade, estado, cep) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
    
    def mostrar_endereco(self):
        print("Endereco: ", end="")
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")