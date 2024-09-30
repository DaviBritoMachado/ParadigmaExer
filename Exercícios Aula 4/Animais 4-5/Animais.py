# 4. Herança Crie uma classe base Animal com métodos como som. Derive classes como
# Cachorro e Gato que implementam o método som de maneiras diferentes.
# 5. Polimorfismo Utilize polimorfismo para criar uma função que receba uma lista de
# objetos Animal e chame o método som de cada um, demonstrando comportamento
# diferente para cada subclasse.

class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
class Galinha(Animal):
    def emitir_som(self):
        return "Cocorico"
    
def som_todos_animais(lista):
    for animal in lista:
        print(animal.emitir_som())
    
def main():
    cachorro = Cachorro("Buldog", "Tobi")
    gato = Gato("Laranja", "Morte")
    galinha = Galinha("Branca", "Gala")

    som_todos_animais([cachorro, gato, galinha])

if __name__ == "__main__":
    main()
    