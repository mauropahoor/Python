'''
20)Faça um programa que leia um número binário qualquer e calcule o seu decimal correspondente.
'''
n = int(input())
dec = 0
i = 0

while(n > 0):
    dec += (n % 10) * (2 ** i) 
    n //= 10
    i += 1
print(dec)