'''
16)Faça um programa que calcule o fatorial de vários números.
Quando for lido um número menor que zero, o programa termina.
'''
while(n != 0):
    n = int(input())
    fat = 1
    while(n != 1):
        fat *= n
        n -= 1
    print(f"{fat}") 
