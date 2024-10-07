package main

import (
	"fmt"
	"math/rand"
)

func gerar_cartela() {
	cartela := map[int]bool{}

	while len(cartela) < 25{
		x = rand.Intn(99)
		cartela[x] := true
	}

	return cartela
}

func imprimir_cartela(cartela) {
	fmt.Println("Cartela de bingo: ")
	x = 0 int
	for j, _ := range cartela{
		fmt.Print(j)
		x++
		if(x % 5 == 0){
			fmt.Println()
		}
	}

}

func main() {
	cartela = gerar_cartela()
	imprimir_cartela()
}