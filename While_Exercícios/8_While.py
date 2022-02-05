'''
8) Faça um programa que leia 100 números inteiros e diga quantos são ímpares.
'''

n = 0
i = 0
nImpar = 0

while(i != 100):
    n = int(input())
    if(n % 2 != 0):
        nImpar += 1
    i += 1
print(f"{nImpar}")

