"""
3. 
Dado o programa abaixo, construa a função recursiva mostra( ), que dado um número n positivo natural, escreva a sequência abaixo.  
(no exemplo abaixo n=5) 5 4 3 2 1 2 3 4 5 
num=int(input('Entre com um numero: ')) 
mostra(num) 
"""

def seq(n):
    if (n == j - (j * 2 + 1)):
        return 1
    elif(n < 1):
        if(n != 0):    
            print(n - n - n)
            return seq(n - 1)
        else:
            return seq(n - 2)
    else:
        print(n)
        return seq(n - 1)
j = int(input())
seq(j)