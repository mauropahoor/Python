'''10) Faça um programa que leia um número inteiro e  calcule o seu fatorial. '''

n = int(input())
fat = 1

for i in range (1, n + 1):
    fat *= i
print(fat)