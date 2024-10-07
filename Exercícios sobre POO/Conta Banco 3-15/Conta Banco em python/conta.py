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
