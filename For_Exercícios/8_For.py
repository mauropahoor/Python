'''8) Faça um programa que leia 100 números inteiros e diga quantos são ímpares.'''

count = 0

for i in range(100):
    n = int(input())
    if(n % 2 != 0):
        count += 1
print(count)