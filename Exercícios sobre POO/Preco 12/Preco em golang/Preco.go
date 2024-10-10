package main

import (
	"fmt"
	"math"
)

type Produto struct {
	nome  string
	preco float64
}

func NovoProduto(nome string, preco float64) *Produto {
	return &Produto{nome: nome, preco: preco}
}

func (p1 *Produto) Adicionar(p2 *Produto) string {
	preco := math.Round((p1.preco+p2.preco)*100) / 100 //Arredonda para duas casas decimais
	return fmt.Sprintf("R$%.2f", preco)
}

func main() {
	prod1 := NovoProduto("maçã", 2.01)
	prod2 := NovoProduto("banana", 1.55)

	fmt.Println(prod1.Adicionar(prod2))
}
