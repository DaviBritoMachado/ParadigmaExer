// 3. Encapsulamento Implemente uma classe ContaBancaria com atributos saldo, titular e
// métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.
// 15. Exceções/Erros Personalizados Crie uma classe de exceção personalizada
// SaldoInsuficienteException que seja lançada quando houver uma tentativa de saque
// superior ao saldo disponível na classe ContaBancaria

package main

import (
	"fmt"
)

type SaldoInsuficienteException struct{}

func (e SaldoInsuficienteException) Error() string {
	return "Saldo insuficiente"
}

type ContaBancaria struct {
	titular string
	saldo   float64
}

func NovoContaBancaria(titular string, saldo float64) *ContaBancaria {
	return &ContaBancaria{titular: titular, saldo: saldo}
}

func (c *ContaBancaria) Sacar(valor float64) error {
	if c.saldo >= valor {
		c.saldo -= valor
		fmt.Printf("Você sacou R$%.2f ", valor)
		fmt.Printf("ficando com um saldo de R$%.2f\n", c.saldo)
		return nil
	}
	return SaldoInsuficienteException{}
}

func (c *ContaBancaria) Depositar(valor float64) {
	c.saldo += valor
	fmt.Printf("Você depositou R$%.2f ", valor)
	fmt.Printf("ficando com um saldo de R$%.2f\n", c.saldo)
}

func main() {
	conta := NovoContaBancaria("Jorge", 200.0)
	err := conta.Sacar(550.37)
	if err != nil {
		fmt.Println(err)
	}
}
