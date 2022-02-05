"""
1. Classe Triangulo: Crie uma classe que modele um triangulo:
    –Atributos: LadoA, LadoB, LadoC
    –Métodos: calcular Perímetro, MaiorLado;
Crie um programa que utilize esta classe. 
Ele deve pedir ao usuário que informe as medidas de um triangulo. 
Depois, deve criar um objeto com as medidas e imprimir seu perímetro e o maior lado.
"""

class triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    def maior_lado(self):
        if(self.ladoA > self.ladoB and self.ladoA > self.ladoC):
            return self.ladoA
        elif(self.ladoB > self.ladoA and self.ladoB > self.ladoC):
            return self.ladoB
        else:
            return self.ladoC

a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

t1 = triangulo(a,b,c)

print("O perimetro do triangulo é ",t1.perimetro())
print("O maior lado do triangulo é ",t1.maior_lado())