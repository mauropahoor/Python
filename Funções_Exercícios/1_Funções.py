"""
1. Faça uma função que retorne o valor absoluto de um número
"""

def valorAbsoluto(x):
    if(x >= 0):
        return x
    else:
        return x - 2 * x
n = int(input("Insira o numero para retornar seu valor absoluto "))
print("O valor absoluto é", valorAbsoluto(n))