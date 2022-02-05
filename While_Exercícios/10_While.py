'''
10) Faça um programa que leia um número inteiro e  calcule o seu fatorial. 
'''

n = int(input())
fat = n

while(n != 1):
    n -= 1
    fat *= n
print(f"{fat}")

