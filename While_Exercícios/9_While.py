'''
9) Faça um programa que leia 100 números e diga quantos estão acima de 1000, quantos são iguais a 1000 e quantos estão abaixo de 1000.
'''

n = 0
maiorqueMil = 0
menorqueMil = 0
igualMil = 0
i = 0

while(i != 100):
    n = int(input())
    if(n > 1000):
        maiorqueMil += 1
    elif(n == 1000):
        igualMil += 1
    elif(n < 1000):
        menorqueMil += 1
    i += 1
print(f"Maiores que 1000: {maiorqueMil}\nIguais a 1000: {igualMil}\n Menores que 1000: {menorqueMil}")