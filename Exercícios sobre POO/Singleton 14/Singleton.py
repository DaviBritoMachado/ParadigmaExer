# 14. Singleton Implemente o padrão de projeto Singleton para garantir que apenas uma
# instância de uma classe Configuracao seja criada.

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class Configuracao:
    __metaclass__ = Singleton

    def __init__(self) -> None:
        self.ligado = False

    def ligar(self):
        self.ligado = True

def main():
    conf = Configuracao
    confa = Configuracao
    conf.ligar(conf)
    print(confa.ligado)

if __name__ == "__main__":
    main()