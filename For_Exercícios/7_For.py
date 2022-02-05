'''7) Faça um programa que leia 100 números inteiros e diga qual é o menor. '''

n = int(input())
menor = n

for i in range(99):
    n = int(input())
    if(n < menor):
        menor = n
print(menor)