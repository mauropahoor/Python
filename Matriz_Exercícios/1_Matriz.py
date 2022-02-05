"""
1.Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um número k. 
Imprima a matriz na tela antes e depois da multiplicação.
"""
tam = 3
matriz = []


for i in range(tam):
    linha = []
    for j in range(tam):
        element = int(input(f"Digite o termo [{i}][{j}] da matriz: "))
        linha.append(element)
    matriz.append(linha)
k = int(input("Digite o número para multiplicar a matriz:"))
print("Matriz antes da multiplicação:")
for i in range(tam):
    print(matriz[i])
for i in range(len(matriz)):
    matriz[i][i] *= k
print("Matriz depois da multiplicação:")
for i in range(tam):
    print(matriz[i])
