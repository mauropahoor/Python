'''12) Faça um programa que leia um número é verifique se ele é um número primo.'''

n = int(input())
j = 1
divisores = 0

for i in range(n):
    if(n % j == 0):
        divisores += 1
    j += 1
if(divisores == 2):
    print("Primo")
else:
    print("Composto")