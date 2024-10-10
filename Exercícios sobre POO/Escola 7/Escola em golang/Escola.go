// 7. Associação Crie uma classe Escola e uma classe Professor. A associação deve permitir
// que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

package main

import "fmt"

type Escola struct {
	nome      string
	contratos []*Professor
}

type Professor struct {
	nome      string
	contratos []*Escola
}

func Novo_escola(nome string) *Escola {
	return &Escola{nome: nome}
}

func Novo_professor(nome string) *Professor {
	return &Professor{nome: nome}
}

func contrato_escola_professor(escola *Escola, professor *Professor) {
	escola.contratos = append(escola.contratos, professor)
	professor.contratos = append(professor.contratos, escola)
}

func imprimir_contratos_escola(escola *Escola) {
	fmt.Printf("%s tem contrato com ", escola.nome)
	for _, parceiro := range escola.contratos {
		fmt.Printf("%s ", parceiro.nome)
	}
}

func imprimir_contratos_professor(professor *Professor) {
	fmt.Printf("%s tem contrato com ", professor.nome)
	for _, parceiro := range professor.contratos {
		fmt.Printf("%s ", parceiro.nome)
	}
}

func main() {
	escola1 := Novo_escola("Ensino")
	escola2 := Novo_escola("Felicidade")

	prof1 := Novo_professor("Jorge")
	prof2 := Novo_professor("Iranildo")

	contrato_escola_professor(escola1, prof1)
	contrato_escola_professor(escola2, prof1)
	contrato_escola_professor(escola1, prof2)

	imprimir_contratos_professor(prof1)
	imprimir_contratos_escola(escola1)
}
