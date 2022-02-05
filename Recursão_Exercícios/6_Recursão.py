"""
6. Os primeiros membros da associação de Pitágoras definiram números poligonais como sendo o número de pontos em determinadas configurações geométricas. 
Os primeiros números pentagonais  são 1, 5, 12, 22. 
Faça uma função recursiva que receba um número natural positivo e encontre o n-ésimonúmero pentagonal.
"""

def pent(n):
    return (3 * (n **2) - n)/2
j = int(input())
print(pent(j))