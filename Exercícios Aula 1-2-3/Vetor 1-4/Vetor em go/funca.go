package funca

import (
	"fmt"
	"math/rand"
)

func faz_lista(x){
	vetor := [x]int{}

	fmt.Println("Digite %d números inteiros:", x)

	for i := 0; i < x; i++ {
		fmt.Scan(&vetor[i])
	}

	return vetor
} 

func faz_lista_aleatoria(x){
	vetor := [x]int{}

	for i := 0; i < x; i++ {
		vetor[i]
	}

	return vetor
}

func exibicao(vetor){
	for _, valor := range vetor{
		fmt.Printf("%d", valor)
	}
}

func maior_menor(vetor){
	maiorValor := vetor[0]
	menorValor := vetor[0]

	for _, valor := range vetor {
		soma += valor
		if valor > maiorValor {
			maiorValor = valor
		}
		if valor < menorValor {
			menorValor = valor
		}
	}
	fmt.Printf("Maior valor: %d\n", maiorValor)
	fmt.Printf("Menor valor: %d\n", menorValor)
}