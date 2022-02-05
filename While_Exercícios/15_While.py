'''
15) Faça um programa que leia a altura e o sexo (codificado em 1=masculino e 2=feminino) de um grupo de n pessoas lidas do teclado. 
Calcule e escreva:
a) Média da altura dos grupo
b) Média da altura dos homens
c) Média da altura das mulheres
d) Maior altura do grupo
e) Menor altura do grupo
'''
n = int(input())
m = 0
f = 0
bothMed = 0
mascMed = 0
femMed = 0
alt = float(input())
sex = float(input())
maior = 0
menor = alt
i = 0


while(i < n - 1):
    alt = float(input())
    sex = float(input())
    if(sex == 1):
        m += 1
        mascMed += alt
        if(alt > maior):
            maior = alt
        elif(alt < menor):
            menor = alt
    if(sex == 2):
        f += 1
        femMed += alt
        if(alt > maior):
            maior = alt
        elif(alt < menor):
            menor = alt
    i += 1
print(f"a) Média de altura do grupo {(mascMed+femMed)/n}\nb)Média de altura dos homens {mascMed/m}\nMédia de altura das mulheres {femMed/f}\nMaior {maior}\nMenor {menor}")
