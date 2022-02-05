'''
Faça um programa que leia um número real x e um número inteiro y e calcule x elevado a y. 
Obs.: Não é permitido a utilização do operador **.
'''
x = float(input())
y = int(input())
i = 1

while(i < y):
    x *= y
    i += 1
print(x) 