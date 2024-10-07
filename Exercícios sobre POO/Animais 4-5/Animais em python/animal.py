class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome
    
    def emitir_som(self):
        pass
    
def som_todos_animais(lista):
    for animal in lista:
        print(animal.emitir_som())