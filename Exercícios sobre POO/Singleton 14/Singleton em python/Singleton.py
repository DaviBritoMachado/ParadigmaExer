# 14. Singleton Implemente o padrão de projeto Singleton para garantir que apenas uma
# instância de uma classe Configuracao seja criada.

from configuracao import Configuracao

def main():
    conf = Configuracao
    confa = Configuracao
    conf.ligar(conf)
    print(confa.ligado)

if __name__ == "__main__":
    main()