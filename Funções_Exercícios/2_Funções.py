"""
2. Faça uma função que receba um número inteiro e retorne Truese o número for par e False se o número for ímpar
"""
def parImpar(x):
    if(x % 2 == 0):
        return True
    else:
        return False
n = int(input("Digite um numero "))
if(parImpar(n)):
    print(f"O número {n} é par")
else:
    print(f'O número {n} é impar')
