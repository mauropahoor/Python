'''9) Faça um programa que leia 100 números e diga quantos estão acima de 1000, quantos são iguais a 1000 e quantos estão abaixo de 1000.'''

maior1000 = 0
menor1000 = 0
igual1000 = 0

for i in range(100):
    n = int(input())
    if(n > 1000):
        maior1000 += 1
    elif(n < 1000):
        menor1000 += 1
    elif(n == 1000):
        igual1000 += 1
print(f">1000 --> {maior1000}, <1000 --> {menor1000}, ==1000 --> {igual1000}")        