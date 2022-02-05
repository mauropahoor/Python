"""
5. Faça um programa que leia um vetor vetde 20 números inteiros. 
O programa deve gerar, a partir do vetor lido, um outro vetor posque contenha apenas os valores inteiros positivos de vet. 
A partir do vetor pos, deve ser gerado um outro vetor semdupque contenha apenas uma ocorrência de cada valor de pos.
"""

tam = 5
vet = [0] * tam
pos = []
for i in range(len(vet)):
    vet[i] = int(input(f"Digite o valor {i} do vetor\n"))
    if(vet[i] >= 0):
        pos.append(vet[i])
j = 0
cont = 0
sendup = []
while(j != len(pos)):
    if(cont == 0):
        sendup.append(pos[j])
    cont = 0
    for i in range(len(pos)):
        if(sendup[j] == pos[i] and i != j):
            cont += 1
    j += 1
print(f"O vetor Vet = {vet}, o vetor Pos = {pos}, o ventor Sendup = {sendup}")
