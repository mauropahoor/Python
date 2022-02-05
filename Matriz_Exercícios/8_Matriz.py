"""
8. Faça um programa que lê duas notas para cada aluno de duas turmas. 
Cada turma tem 3 alunos. Armazene os dados em uma matriz M. 
Cada aluno deve ter três notas (as duas digitadas e a média dessas duas). 
Calcule a média de cada turma e armazene em um vetor TURMA. 
Informe qual turma tem maior média, e quais alunos tiveram média maior que a média de sua turma.
"""

student = 2
notes = []
classes = 2
test = 2
turma = [0] * classes
med_class = 0

for l in range(classes):
    for i in range(student):
        line = []
        med_class = 0
        for j in range(test):
            n = int(input(f"Digite a nota {j + 1} do aluno {i + 1} da turma {l + 1}: "))
            line.append(n)
            med_class += n
        med_class /= student
        line.append(med_class)
        notes.append(line)
        turma[l] += notes[i][len(notes[0]) - 1]/student
best_med = turma[0]
for i in range(len(turma)):
    if(turma[i] > best_med):
        best_med_class = i
        best_med = turma[i]
print(f"A turma que obteve a melhor média foi a turma {i + 1}.")
for i in range(student * classes):
    if(notes[i][test] > best_med):
        print(f"O aluno {i + 1} está acima da média da turma.")
    