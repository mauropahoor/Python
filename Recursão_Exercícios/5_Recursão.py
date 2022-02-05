"""
5. Os primeiros membros da associação de Pitágoras definiram números poligonais como sendo o número de pontos em determinadas configurações geométricas. 
Os primeiros números triangulares são 1, 3, 6, 10, 15. 
Faça uma função recursiva que receba um número natural positivo e encontre o n-ésimonúmero triangular.
"""

def triang(n):
    if(n == 1):
        return 1
    else:
        return n + triang(n - 1)
j = int(input())
print(triang(j))