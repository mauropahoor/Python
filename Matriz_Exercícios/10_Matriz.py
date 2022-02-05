"""
10.Um quadrado mágico, é uma matriz quadrada, cuja a soma de cada linha, coluna ou diagonal é a mesma. 
Faça um programa que leia uma matriz 50x50, e diga se essa matriz é um quadrado mágico.
Exemplo de um quadrado mágico 4x4. 
A soma de qualquer linha,coluna ou diagonal da sempre 34.
16    2    3    13
5     11   10    8
9     7    6    12
4     14   15    1
"""

matriz = []
tam = 4
som_line = 0
som_col = 0
som_dia = 0

for i in range(tam):
    line = []
    for j in range(tam):
        n = int(input("Insira o termo na matriz: "))
        line.append(n)
    matriz.append(line)
for i in range(tam):
    for j in range(tam):
        som_line += matriz[i][j]
        som_col += matriz[j][i]
        som_dia += matriz[j][j]
if(som_line == som_col == som_dia):
    print("Esta matriz é um quadrado mágico.")