// Davi Brito Machado
// 30116104

package main

import "fmt"

// Definindo a estrutura Retangulo
type Retangulo struct {
	comprimento, largura float64
}

// Função para calcular a área do retângulo
func (r Retangulo) calcularArea() float64 {
	return r.comprimento * r.largura
}

// Função para calcular o perímetro do retângulo
func (r Retangulo) calcularPerimetro() float64 {
	return 2 * (r.comprimento + r.largura)
}

// Definindo a estrutura Triangulo
type Triangulo struct {
	lado1, lado2, lado3 float64
}

// Função para calcular a área do triangulo
func(t Triangulo) calcularPerimetro() float64 {
	return t.lado1 + t.lado2 + t.lado3
}

// Função para veriricar o tipo do triangulo
func (t Triangulo) tipo() string {
	if t.lado1 == t.lado2 && t.lado1 == t.lado3 {
		return "Equilátero"
	} else if t.lado1 == t.lado2 || t.lado1 == t.lado3 || t.lado2 == t.lado3 {
		return "Isósceles"
	} else {
		return "Escaleno"
	}
}

func main() {
	// Criando uma instância da estrutura Retangulo
	ret := Retangulo{comprimento: 200, largura: 300}
	fmt.Printf("Área: %.2f\n", ret.calcularArea())
	fmt.Printf("Perímetro: %.2f\n", ret.calcularPerimetro())
	// Criando uma instância da estrutura Triangulo
	tri := Triangulo{lado1: 200, lado2: 300, lado3: 200}
	fmt.Printf("Tipo: %s\n", tri.tipo())
	fmt.Printf("Perímetro: %.2f\n", tri.calcularPerimetro())
}
