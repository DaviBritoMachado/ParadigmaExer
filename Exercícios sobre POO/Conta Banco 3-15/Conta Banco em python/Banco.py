# 3. Encapsulamento Implemente uma classe ContaBancaria com atributos saldo, titular e
# métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.
# 15. Exceções/Erros Personalizados Crie uma classe de exceção personalizada
# SaldoInsuficienteException que seja lançada quando houver uma tentativa de saque 
# superior ao saldo disponível na classe ContaBancaria

from conta import Conta_Bancaria

def main():
    conta = Conta_Bancaria("Jorge", "200")
    conta.sacar(550.37)

if __name__ == "__main__":
    main()