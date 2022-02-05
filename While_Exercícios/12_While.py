'''
12) Faça um programa que leia um número é verifique se ele é um número primo.
'''

n = int(input())
primo = 0
i = 2

while(i < n):
    if(n % i == 0):
        primo += 1
    i += 1
if(primo > 0):
    print("O número não é primo")
else:
    print("O número é primo")


