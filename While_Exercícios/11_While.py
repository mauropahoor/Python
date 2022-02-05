'''
11) Faça um programa que leia um número inteiro e calcule e mostre os n primeiros termos da série de Fibonacci. 
'''

aux = 0
n1 = 0
n2 = 1
n = int(input())
i = 0

if(n == 1): #Caso só tiver 1 caso, imprimir apenas o primeiro termo
   print(0)
   i += 1
else: #Caso for mais de 1 caso, imprimir os 2 primeiros termos e ja adiciona-los no contador 
    print(f"{n1}\n{n2}")
    i += 2
while(i < n):
    aux = n1 + n2 #Fazer e imprimir a soma dos 2 termos anteriores
    print(aux)
    n1 = n2 #Fazer o n1 virar o termo anterior ao aux
    n2 = aux#Fazer o n2 virar o aux, para assim descobrir o proximo termo da sequencia
            #ao fazer a soma
    i += 1
