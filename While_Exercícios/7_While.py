'''
7) Faça um programa que leia 100 números inteiros e diga qual é o menor. 
'''

n = int(input())

menor = n

i = 0

while(i != 99):
    n = float(input())
    if(n < menor):
        menor = n
    i += 1
print(f"{menor}")