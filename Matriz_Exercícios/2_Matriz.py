"""
2.Faça um programa que leia duas matrizes A e B 2x2 e imprima a matriz C que é a soma das matrizes A e B.
"""

tam = 2
matriz_a = []
matriz_b = []
matriz_c = []

for i in range(tam):
    linha = []
    for j in range(tam):
        n = int(input(f"Digite a linha {i}, coluna {j} da matriz A: "))
        linha.append(n)
    matriz_a.append(linha)
for i in range(tam):
    linha = []
    for j in range(tam):
        n = int(input(f"Digite a linha {i}, coluna {j} da matriz B: "))
        linha.append(n)
    matriz_b.append(linha)
print("Matriz A:")
for i in range(tam):
    print(matriz_a[i])
print("Matriz B:")
for i in range(tam):
    print(matriz_b[i])
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(matriz_a[i][j] + matriz_b[i][j])
    matriz_c.append(linha)
print("Matriz C:")
for i in range(tam):
    print(matriz_c[i])