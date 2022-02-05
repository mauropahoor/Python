"""
2. 
Faça uma função recursiva que calcule e retorne x elevado a z. 
Em seguida, apresente o passo a passo de execução do programa com x=2 e z=-2. 
Obs.: x é um número real e z é um número inteiro. Não use o operador **
    def potencia(x,  z):
"""

def pot(x, z):
    if(z >= 1):
        if(z == 1):
            return x
        else:
            return pot(x * a, z - 1)
    elif(z == 0):
        return 1
    elif(z < 0):
        z += b*-2
        if(z == 1):
            return x
        else:
            return pot(1/x * 1/a, z - 1)
a, b = input().split()
a = int(a)
b = int(b)
print(pot(a, b))