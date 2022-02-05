'''
19)Faça um programa que leia um número binário qualquer e calcule o seu decimal correspondente.
'''
n = int(input())
aux = len(str(n))
i = 0
dec = 0

while(i < aux):
    dec += (n % 10) * (2 ** i)
    n //= 10
    i += 1
print(dec)