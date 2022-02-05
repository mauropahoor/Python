'''14) Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo. 
Ex.: n = 5
*
**
***
****
*****'''

n = int(input())

for i in range(1, n + 1):
    print('*' * i)