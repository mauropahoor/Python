"""
4.Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. 
Imprima na tela a matriz, a linha de maior soma e a soma. 
"""

tam = 3
matriz = []

for i in range(tam):
    linha = []
    for j in range(tam):
        n = int(input(f"Digite o elemento[{i}][{j}] da matriz: "))
        linha.append(n)
    matriz.append(linha)
aux = 0
som = 0
maior = 0
for i in range(tam):
    som = 0
    for j in range(tam):
        som += matriz[i][j]
    if(som > maior):
        maior = som
        aux = i
print("Matriz:")
for i in range(tam):
    print(matriz[i])
print("Linha com maior soma:")
print(matriz[aux])
print(f"A soma é {som}.")