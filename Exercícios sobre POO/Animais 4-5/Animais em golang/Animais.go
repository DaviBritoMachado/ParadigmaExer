package main

import (
	"fmt"
)

type Animal interface {
	EmitirSom() string
}

type Cachorro struct {
	especie string
	nome    string
}

type Gato struct {
	especie string
	nome    string
}

type Galinha struct {
	especie string
	nome    string
}

func (c Cachorro) EmitirSom() string {
	return "Au au"
}

func (g Gato) EmitirSom() string {
	return "Miau"
}

func (g Galinha) EmitirSom() string {
	return "Cocorico"
}

func SomTodosAnimais(lista []Animal) {
	for _, animal := range lista {
		fmt.Println(animal.EmitirSom())
	}
}

func main() {
	cachorro := Cachorro{"Buldog", "Tobi"}
	gato := Gato{"Laranja", "Morte"}
	galinha := Galinha{"Branca", "Gala"}

	SomTodosAnimais([]Animal{cachorro, gato, galinha})
}
