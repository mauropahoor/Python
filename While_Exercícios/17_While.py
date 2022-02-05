'''
17)Faça um programa que leia um número inteiro n e mostre os n primeiros números primos na tela.
'''
n = int(input())
i = 0
test = 2

while(i < n):
    pCheck = 0
    div = 2
    while(div != test):
        if(test % div == 0):
            pCheck += 1
        div += 1
    if(pCheck == 0):
        print(test)
        i += 1
    test += 1