"""
1.Faça um programa que leia dois vetores de 3 posições, que representam forças sobre um ponto no espaço 3D, e escreva a força resultante. 
Dica: força resultante é obtida pela soma dos valores das coordenadas correspondentes nos dois vetores: 
(x1 + x2), (y1+ y2), (z1 + z2)
"""
tam = 3

vet1 = [0] * tam
vet2 = [0] * tam
vet3 = [0] * tam

for i in range(len(vet1)):
    vet1[i] = int(input(f"Entre com o valor {i + 1} do vet1:\n"))
for i in range(len(vet2)):
    vet2[i] = int(input(f"Entre com o valor {i + 1} do vet2:\n"))
for i in range(len(vet3)):
    vet3[i] += vet1[i] + vet2[i]
print(vet3)