"""
3.Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes. 
Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes. 
Imprima as matrizes A, B e a matriz resultante da multiplicação.
"""

matriz_a = []
matriz_b = []
matriz_c = []
l = int(input("Digite a quantidade de linhas de A: "))
c = int(input("Digite a quantidade de colunas de A: "))
i = 0

for i in range(l):
    linha = []
    for j in range(c):
        n = int(input(f"Digite o termo[{i}][{j}] de A: "))
        linha.append(n)
    matriz_a.append(linha)    
l = int(input("Digite a quantidade de linhas de B: "))
c = int(input("Digite a quantidade de colunas de B: "))
for i in range(l):
    linha = []
    for j in range(c):
        n = int(input(f"Digite o termo[{i}][{j}] de B: "))
        linha.append(n)
    matriz_b.append(linha)    
if(len(matriz_a[0]) == len(matriz_b)):
    for i in range(len(matriz_a)):
        linha = []
        for k in range(len(matriz_b[0])):        
            som = 0
            for j in range(len(matriz_a[0])):
                n = (matriz_a[i][j] * matriz_b[j][k])
                som += n
            linha.append(som)
        matriz_c.append(linha)
    print("Matriz A:")
    for i in range(len(matriz_a)):
        print(matriz_a[i])
    print("Matriz B:")
    for i in range(len(matriz_b)):
        print(matriz_b[i])
    print("Matriz A * B:")
    for i in range(len(matriz_c)):
        print(matriz_c[i])
else:
    print("Não é possivel multiplicar essas matrizes.")