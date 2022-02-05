"""
5.Faça um programa que leia a ordem de uma matriz quadrada A (até 100), posteriormente leia seus valores e escreva sua transposta AT, onde AT[i][j] = A[j][i]
"""

tam = int(input("Digite o tamanho da matriz quadrada: "))
matriz = []
matriz_transposta = []

for i in range(tam):
    linha = []
    for j in range(tam):
        n = int(input(f"Digite o termo[{i}][{j}] da matriz: "))
        linha.append(n)
    matriz.append(linha)
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(matriz[j][i])
    matriz_transposta.append(linha)
for i in range(tam):
    print(matriz_transposta[i])