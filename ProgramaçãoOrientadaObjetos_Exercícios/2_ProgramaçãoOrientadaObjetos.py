"""
2.Classe Funcionário: 
Implemente a classe Funcionário. 
Um funcionário tem um nome e um salário. 
Escreva um construtor com dois parâmetros (nome e salário) e o método aumentarSalario(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem. 
Exemplo de uso:
    harry=funcionário("Harry",25000)
    harry.aumentarSalario(10)
Faca um programa que teste o método da classe.
"""

class funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    
    def getSalario(self):
        print("O salário é",self.salario)


    def setSalario(self, x):
        self.salario += self.salario * 0.10
        return self.salario
    
nome = input("Digite o nome: ")
salario = int(input("Digite o salario: "))
f1 = funcionario(nome,salario)

f1.getSalario()
print("Salario com 10% de aumento", f1.setSalario(10))
        