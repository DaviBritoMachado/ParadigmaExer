from funcionario_abs import Funcionario
    
class Funcionario_assalariado(Funcionario):
    def calcular_salario(self, preco_hora, dias):
        return preco_hora * 8 * dias