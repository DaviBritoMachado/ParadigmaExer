// 10. Sobrecarga de Métodos (Java) / Métodos com Nomes Diferentes (Python, Go)
// Implemente uma classe Calculadora com métodos somar que aceita diferentes números
// de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
// para diferentes quantidades de parâmetros.
// 13. Métodos Estáticos Adicione um método estático à classe Matematica que calcula o
// fatorial de um número. Em Python, utilize @staticmethod, em Java static, e em Golang crie
// uma função regular na struct.

package main

import "fmt"

type Calculadora struct {
}

func (c Calculadora) soma(x, y int) int {
	return x + y
}

func (c Calculadora) soma3(x, y, z int) int {
	return x + y + z
}

func fatorial(x int) int {
	fator := 1
	for x > 0 {
		fator *= x
		x -= 1
	}
	return fator
}

func main() {
	calc := Calculadora{}
	fmt.Println(calc.soma(1, 2))
	fmt.Println(calc.soma3(1, 2, 3))

	fmt.Println(fatorial(4))
}
