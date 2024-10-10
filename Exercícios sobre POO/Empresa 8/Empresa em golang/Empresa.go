// 8. Agregação Modele uma classe Empresa que agregue uma lista de objetos Empregado.
// Cada empregado deve ter atributos como nome e cargo

package main

import "fmt"

type Endereco struct {
	Rua    string
	Cidade string
	Estado string
	CEP    string
}

func (e Endereco) mostrarEndereco() {
	fmt.Printf("Rua: %s, Cidade: %s, Estado: %s, CEP: %s\n", e.Rua, e.Cidade, e.Estado, e.CEP)
}

type Funcionario struct {
	Nome     string
	cargo    string
	salario  string
	Endereco *Endereco
}

func (p *Funcionario) adicionarEndereco(endereco *Endereco) {
	p.Endereco = endereco
}

func (p Funcionario) mostrarInformacoes() {
	fmt.Printf("Nome: %s, Cargo: %s, Salario: %s\n", p.Nome, p.salario)
	if p.Endereco != nil {
		fmt.Println("Endereço:")
		p.Endereco.mostrarEndereco()
	} else {
		fmt.Println("Endereço não disponível")
	}
}

type Empresa struct {
	Nome         string
	CNPJ         string
	Funcionarios []Funcionario
}

func (e *Empresa) contratarFuncionario(funcionario Funcionario) {
	e.Funcionarios = append(e.Funcionarios, funcionario)
}

func (e Empresa) listarFuncionarios() {
	fmt.Printf("Funcionários da empresa %s:\n", e.Nome)
	for _, funcionario := range e.Funcionarios {
		fmt.Println(funcionario.Nome)
	}
}

func main() {
	endereco1 := Endereco{"Av. Principal", "Patapingas", "Minas Gerais", "12345-234"}
	funcionario1 := Funcionario{"João", "Faxineiro", "R$1500,00", nil}
	funcionario1.adicionarEndereco(&endereco1)

	endereco2 := Endereco{"Av. Secundaria", "Maraja", "Sao paulo", "54321-234"}
	funcionario2 := Funcionario{"Maria", "Gerente", "R$18000,00", nil}
	funcionario2.adicionarEndereco(&endereco2)

	empresa := Empresa{"Empresa ABC", "18509274", []Funcionario{}}
	empresa.contratarFuncionario(funcionario1)
	empresa.contratarFuncionario(funcionario2)

	empresa.listarFuncionarios()
}
