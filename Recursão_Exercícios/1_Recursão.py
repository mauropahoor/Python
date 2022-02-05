"""
1. Faça uma função recursiva que receba um número inteiro e calcule a soma dos n primeiros números inteiros.
"""

def soma(n):
    if(n == 1):
        return 1
    else:
        return n + soma(n - 1)
x = int(input())
print(soma(x))