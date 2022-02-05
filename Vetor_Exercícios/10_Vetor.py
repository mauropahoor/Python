"""
10. Existem 20 candidatos à presidência, com códigos que variam de 1 até 20. Codificou-se 21 para votos brancos e 22 para votos nulos. 
Cada voto vem em um cartão (contendo só um voto) e o último cartão vem com o número 0 (zero). 
Faça um programa que auxilie a operação dos votos, imprimindo a quantidade de votos de cada candidato, o número de votos em branco, o número de votos nulos e o total de votantes. 
Imprima também o(s) candidato(s) que venceram a eleição e o número de votos do(s) vencedor(es).
"""

votos = []
cont = 0
voteCont = 0

while (votos.count(0) == 0): #inserir os votos
    votos.append(int(input("Insira seu voto\n")))
    cont += 1
voteCont = [0] * 23 #fazer o vetor ir de 0 até 22
for i in range(1, len(votos) + 1):
        voteCont[i] += votos.count(i) #No espaço i, pegar a quantidade de votos i no vetor. Ex: VoteCont[1] += todos os votos 1 do vetor votos
for i in range(1, len(voteCont)):
    if(i <= 20): #Imprimir os resultados
        print(f"O canditado {i} teve {voteCont[i]} votos")
    elif(i == 21):
        print(f"Houve {voteCont[i]} votos brancos")
    else:
        print(f"Houve {voteCont[i]} votos nulos")
print(f"Número de votos: {cont - 1}")