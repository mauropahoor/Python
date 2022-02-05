"""
7.Dado o programa abaixo, reescreva a função perfeito(), sem utilizar nenhuma estrutura de repetição.
def perfeito(n, i=1, cont=0):
    for i in range (1,n):
        if((n%i)==0):
            cont+=i;
        if(cont==n):
            print('É um número perfeito')
        else:
            print('Não é um número perfeito')  
n=int(input('Entre com um número: '))
perfeito(n, 1, 0)
"""

def perfeito(n, i=1, cont=0):
    if(i == n):
        if(cont==n):
            print('É um número perfeito')
        else:print('Não é um número perfeito')  
        return 1
    elif((n%i)==0):
        cont += i
        return perfeito(n, i+1, cont)
    else:
        return perfeito(n, i+1, cont)

n=int(input('Entre com um número: '))
perfeito(n, 1, 0)