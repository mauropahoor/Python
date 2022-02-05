"""
6. Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. 
Ao final, o programa deve informar:
    a. De quem foi a melhor volta da prova, e em que volta
    b. Classificação final em ordem (1º o campeão)
    c. Qual foi a volta com a média mais rápida
"""

scoreboard = []
aux = 0
med = 0
best_time = 0
best_time_name = ""
best_round_med = 0
best_round = 0
fastest_lap = 0
number_pilots = 6
number_rounds = 10

for i in range(number_pilots):
    line = []
    name = input("Digite o nome do corredor: ")
    line.append(name)
    for j in range(number_rounds):
        time = float(input(f"Digite o tempo de cada volta do corredor {name}: "))
        if(aux == 0):
            best_time = time
            best_time_name = name
            best_round = j  
            aux += 1
        line.append(time)
        if(time < best_time):
            best_time = time
            best_time_name = name
            best_round = j        
    scoreboard.append(line)
for j in range(1, number_rounds + 1):
    for i in range(number_pilots):
        med += scoreboard[i][j]
    med /= number_pilots
    if(aux == 1):
        best_round_med = med
        fastest_lap = j
        aux += 1
    if(med < best_round_med):
        fastest_lap = j
print(f"A melhor volta foi do(a) {best_time_name[0].upper() + best_time_name[1:len(best_time_name)]}, na volta {best_round + 1}, com o tempo {best_time}.")
print(f"A volta com a média mais rápida foi a {fastest_lap}.")
        