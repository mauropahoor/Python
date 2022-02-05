"""
Faça um programa que preencha um vetor com vários valores inteiros lidos do teclado. 
A condição de parada será o usuário digitar FIM. 
Em seguida, informe o número de ocorrências de cada elemento do vetor. 
Ex.: Vet = [1, -100, 1, 30, 12, 1, 12, 12, 12, 90] 
Seu programa deverá retornar: 
    O número -100 apareceu 1 vez no vetor 
    O número 1 apareceu 3 vezes no vetor 
    O número 12 apareceu 4 vezes no vetor 
    O número 30 apareceu 1 vez no vetor 
    O número 90 apareceu 1 vez no vetor 
Obs.:  Cada ocorrência do número no vetor, só deve aparecer uma vez na resposta, ou seja, 
não é para o seu programa informar 3 vezes que o número 1 apareceu no vetor, e nem para informar que o número 12 apareceu 4 vezes no vetor. 
"""
#Algoritmos Computacionais e Estruturas de Dados 
#4a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 07/10/2021
#Turma 2BINFO
#Alunos:
#Mauro Campos Pahoor
#Victor Pinheiro Palmeira
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Victor Kauã Martins Nunes
#Questão 1 

vetor=[]
vetor_norepeat=[]
valido=True
while(valido):
    valor=input("Insira um inteiro: ")
    if(valor.lower()=="fim"):
        valido=False
    else:
        vetor.append(int(valor))
for i in range(len(vetor)):
    if(vetor[i] not in vetor_norepeat):
        vetor_norepeat.append(vetor[i])
vetor_norepeat=sorted(vetor_norepeat)
for i in range(len(vetor_norepeat)):
    quant=vetor.count(vetor_norepeat[i])
    if (quant==1):
        print(f"O número {vetor_norepeat[i]} apareceu {quant} vez no vetor")
    else:
        print(f"O número {vetor_norepeat[i]} apareceu {quant} vezes no vetor")