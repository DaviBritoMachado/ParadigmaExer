// 1. Classes e Objetos Básicos Crie uma classe Carro com atributos como marca, modelo, e
// ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.
// 2. Métodos Adicione um método acelerar e frear à classe Carro que altere um atributo
// velocidade. Crie um método para exibir a velocidade atual.
// 6. Composição Implemente uma classe Motor e associe-a a uma classe Carro. A classe
// Carro deve ter um objeto do tipo Motor como um de seus atributos.

package main

import "fmt"

// Struct Motor
type Motor struct {
	tipo     string
	potencia int
	ligado   bool
}

func (m *Motor) Ligar() {
	m.ligado = true
	fmt.Println("O motor está ligado.")
}

func (m *Motor) Desligar() {
	m.ligado = false
	fmt.Println("O motor está desligado.")
}

// Struct Pneu
type Pneu struct {
	marca   string
	tamanho int
}

func (p Pneu) Inflar() {
	fmt.Println("O pneu está inflado.")
}

func (p Pneu) Desinflar() {
	fmt.Println("O pneu está desinflado.")
}

// Struct Carro
type Carro struct {
	marca      string
	modelo     string
	ano        int
	motor      Motor
	pneus      [4]Pneu
	velocidade int
}

func NewCarro(marca, modelo string, ano int) Carro {
	motor := Motor{"Gasolina", 150, false}
	pneus := [4]Pneu{}
	velocidade := 0
	for i := 0; i < 4; i++ {
		pneus[i] = Pneu{"Pirelli", 18}
	}
	return Carro{marca, modelo, ano, motor, pneus, velocidade}
}

func (c Carro) Detalhes() {
	fmt.Printf("Marca : %s ", c.marca)
	fmt.Printf("Modelo : %s ", c.modelo)
	fmt.Printf("Ano : %d \n", c.ano)
}

func (c *Carro) Ligar() {
	c.motor.Ligar()
	fmt.Println("O carro está pronto para rodar.")
}

func (c *Carro) Desligar() {
	c.motor.Desligar()
	fmt.Println("O carro foi desligado.")
}

func (c *Carro) TrocarPneu(indice int, novoPneu Pneu) {
	if indice >= 0 && indice < 4 {
		c.pneus[indice] = novoPneu
		fmt.Printf("Pneu %d trocado.\n", indice+1)
	} else {
		fmt.Println("Índice de pneu inválido.")
	}
}

func (c *Carro) Acelerar() {
	if c.motor.ligado == true {
		c.velocidade += 10
		fmt.Println("O carro está acelerando")
	} else {
		fmt.Println("O carro está desligado")
	}
}

func (c *Carro) Frear() {
	if c.motor.ligado == true {
		if c.velocidade > 0 {
			c.velocidade -= 10
			fmt.Println("O carro está freando")
		} else {
			fmt.Println("O carro está parado")
		}

	} else {
		fmt.Println("O carro está desligado")
	}
}

func (c Carro) Mostrar_velocidade() {
	fmt.Printf("A velociade é de %dKm \n", c.velocidade)
}

func main() {
	carro := NewCarro("Toyota", "Corolla", 2000)
	carro.Detalhes()
	carro.Ligar()
	carro.Acelerar()
	carro.Mostrar_velocidade()
	carro.Frear()

	novoPneu := Pneu{"Michelin", 17}
	carro.TrocarPneu(2, novoPneu)

	carro.Desligar()
}
