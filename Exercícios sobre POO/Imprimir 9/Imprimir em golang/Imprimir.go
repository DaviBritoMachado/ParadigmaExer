package main

import (
	"fmt"
)

type Imprimivel interface {
	Imprimir()
}

type Relatorio struct {
	texto string
}

func Novo_relatorio(texto string) *Relatorio {
	return &Relatorio{texto: texto}
}

func (r *Relatorio) Imprimir() {
	fmt.Println("Relatorio: " + r.texto)
}

type Contrato struct {
	texto string
}

func Novo_contrato(texto string) *Contrato {
	return &Contrato{texto: texto}
}

func (c *Contrato) Imprimir() {
	fmt.Println("Contrato: " + c.texto)
}

func main() {
	relatorio := Novo_relatorio("As vendas diminuíram em 74%, estamos em falência")
	relatorio.Imprimir()

	contrato := Novo_contrato("Nosso contrato com o governo está acabando e eles não querem renovar")
	contrato.Imprimir()
}
