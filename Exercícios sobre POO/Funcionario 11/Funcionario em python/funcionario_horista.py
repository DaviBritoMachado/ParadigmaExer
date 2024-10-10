from funcionario_abs import Funcionario

class Funcionario_horista(Funcionario):
    def calcular_salario(self, preco_hora, hora_dia, dias):
        return preco_hora * hora_dia * dias