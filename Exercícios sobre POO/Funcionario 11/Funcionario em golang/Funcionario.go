// 11. Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
// calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
// implementam calcularSalario de formas distintas.

package main

import (
	"fmt"
)

type Funcionario struct {
	nome  string
	cargo string
}

func (f *Funcionario) CalcularSalario(precoHora float64, args ...int) float64 {
	return 0 // Método abstrato, não deve ser chamado diretamente
}

type FuncionarioHorista struct {
	Funcionario
}

type FuncionarioAssalariado struct {
	Funcionario
}

func (f *FuncionarioHorista) CalcularSalario(precoHora float64, horaDia, dias int) float64 {
	return precoHora * float64(horaDia) * float64(dias)
}

func (f *FuncionarioAssalariado) CalcularSalario(precoHora float64, dias int) float64 {
	return precoHora * 8 * float64(dias)
}

func main() {
	funci1 := &FuncionarioAssalariado{Funcionario{"Jorge", "Professor"}}
	funci2 := &FuncionarioHorista{Funcionario{"Pereira", "Faz-tudo"}}

	fmt.Println(funci1.CalcularSalario(50, 20))
	fmt.Println(funci2.CalcularSalario(70, 4, 4))
}
