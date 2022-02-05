"""
7. Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre: 
    (a) o maior elemento da matriz e sua respectiva posição (linha e coluna); 
    (b) o menor elemento da matriz e sua respectiva posição.
"""

matriz = []
l = 6
c = 3

for i in range(l):
    linha = []
    for j in range(c):
        n = int(input(f"Digite o termo da matriz: "))
        linha.append(n)
    matriz.append(linha)
max = matriz[0][0]
min = matriz[0][0]
i_pos_max = j_pos_max = i_pos_min = j_pos_min = 0
for i in range(l):
    for j in range(c):
        if(matriz[i][j] > max):
            max = matriz[i][j]
            i_pos_max = i
            j_pos_max = j
        if(matriz[i][j] < min):
            min = matriz[i][j]
            i_pos_min = i
            i_pos_min = j
print("Matriz:")
for i in range(len(matriz)):
    print(matriz[i])
print(f"""O maior elemento é {max} que está na posição [{i_pos_max}][{j_pos_max}], 
      o menor elemento é {min} que está na posição [{i_pos_min}][{j_pos_min}]""")