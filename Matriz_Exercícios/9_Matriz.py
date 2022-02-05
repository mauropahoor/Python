"""
9.Faça um programa que leia uma matriz 50x50, e imprima o número de linhas e o número de colunas nulas da matriz. 
Exemplo: matriz 4x4 Essa matriz possui 2 linhas nulas e 1 coluna nula 
1    0    1    -2
4    0    5    6
0    0    0    0
0    0    0    0
"""

matriz = []
tam = 50
l_null = 0
c_null = 0
aux_l = 0
aux_c = 0

for i in range(tam):
    line = []
    for j in range(tam):
        n = int(input(f"Insira o termo na matriz: "))
        line.append(n)
    matriz.append(line)
for i in range(tam):
    aux_c = 0
    aux_l = 0
    for j in range(tam):
        if(matriz[i][j] != 0):
            aux_l += 1
        if(matriz[j][i] != 0):
            aux_c += 1
    if(aux_l == 0):
        l_null += 1
    if(aux_c == 0):
        c_null += 1
print(f"A matriz tem {l_null} linhas nulas e {c_null} colunas nulas.")