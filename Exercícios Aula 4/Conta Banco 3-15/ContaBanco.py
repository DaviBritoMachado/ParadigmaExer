# 3. Encapsulamento Implemente uma classe ContaBancaria com atributos saldo, titular e
# métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.
# 15. Exceções/Erros Personalizados Crie uma classe de exceção personalizada
# SaldoInsuficienteException que seja lançada quando houver uma tentativa de saque 
# superior ao saldo disponível na classe ContaBancaria

class SaldoInsuficienteException(Exception):
    "Saldo insuficiente"
    pass

class Conta_Bancaria:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = float(saldo)
    
    def sacar(self, valor):
        try:
            if(self.saldo > valor):
                self.saldo -= valor
                print("Você sacou R$%.2f " % valor, end="")
                print("ficando com um saldo de R$%.2f" % self.saldo)
            else:
                raise SaldoInsuficienteException
        except SaldoInsuficienteException:
            print ("Saldo insuficiente")

    def depositar(self, valor):
        self.saldo += valor
        print("Você depositou R$%.2f " % valor, end="")
        print("ficando com um saldo de R$%.2f" % self.saldo)

def main():
    conta = Conta_Bancaria("Jorge", "200")
    conta.sacar(550.37)

if __name__ == "__main__":
    main()