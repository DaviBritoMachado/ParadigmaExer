# 11. Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
# calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
# implementam calcularSalario de formas distintas.

from funcionario_assalariado import Funcionario_assalariado
from funcionario_horista import Funcionario_horista    

def main():
    funci1 = Funcionario_assalariado("Jorge", "Professor")
    funci2 = Funcionario_horista("Pereira", "Faz-tudo")

    print(funci1.calcular_salario(50, 20))
    print(funci2.calcular_salario(70, 4, 4))

if __name__ == "__main__":
    main()