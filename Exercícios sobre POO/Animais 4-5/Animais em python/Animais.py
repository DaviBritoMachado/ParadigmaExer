# 4. Herança Crie uma classe base Animal com métodos como som. Derive classes como
# Cachorro e Gato que implementam o método som de maneiras diferentes.
# 5. Polimorfismo Utilize polimorfismo para criar uma função que receba uma lista de
# objetos Animal e chame o método som de cada um, demonstrando comportamento
# diferente para cada subclasse.

from animal import som_todos_animais
from cachorro import Cachorro
from gato import Gato
from galinha import Galinha
    
def main():
    cachorro = Cachorro("Buldog", "Tobi")
    gato = Gato("Laranja", "Morte")
    galinha = Galinha("Branca", "Gala")

    som_todos_animais([cachorro, gato, galinha])

if __name__ == "__main__":
    main()
    