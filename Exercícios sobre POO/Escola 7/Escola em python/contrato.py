def contrato_escola_professor(escola, professor):
    escola.contratos.append(professor)
    professor.contratos.append(escola)

def imprimir_contratos(self):
        print(self.nome + " tem contrato com")
        for parceiro in self.contratos:
            print(parceiro.nome)