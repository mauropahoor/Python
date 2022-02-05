'''
15) Faça um programa que leia a altura e o sexo (codificado em 1=masculino e 2=feminino) de um grupo de n pessoas lidas do teclado. 
Calcule e escreva:
a) Média da altura dos grupo
b) Média da altura dos homens
c) Média da altura das mulheres
d) Maior altura do grupo
e) Menor altura do grupo'''

n = int(input())
sex = 0
altura = 0
h = 0
m = 0
alturah = 0
alturam = 0
totalaltura = 0
maior = 0
aux = 0

for i in range(n):    
    sex = int(input())
    if(sex != 1 and sex != 2):
        print("Sexo invalido")
    else:
        altura = float(input())
        if(aux == 0):
            menor = altura
            aux += 1
        if(altura > maior):
            maior = altura
        if(altura < menor):
            menor = altura
        if(sex == 1):
            alturah += altura
            h += 1
        elif(sex == 2):
            alturam += altura
            m += 1
        totalaltura += altura
print(f"Med homens: {alturah/h:.2f}\nMed mulheres: {alturam/m:.2f}\nMed total: {totalaltura/n:.2f}\nMaior:{maior}\nMenor{menor}") 