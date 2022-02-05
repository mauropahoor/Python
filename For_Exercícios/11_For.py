'''11) Faça um programa que leia um número inteiro e calcule e mostre os n primeiros termos da série de Fibonacci. '''

n = int(input())

t1 = 1
t2 = 1
aux = 0
soma = 0

print(f"{t1}\n{t2}")
for i in range(n - 2):
    soma = t1 + t2
    print(soma)
    t1 = t2
    t2 = soma