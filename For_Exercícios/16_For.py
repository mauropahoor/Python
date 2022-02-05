'''16)Faça um programa que leia um número real x e um número inteiro y e calcule x elevado a y. Obs.: Não é permitido a utilização do operador **.'''

x = int(input())
y = int(input())
z = x

for i in range(1,y):
    x *= z
print(x)