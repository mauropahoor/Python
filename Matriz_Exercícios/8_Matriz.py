"""
8. Faça um programa que lê duas notas para cada aluno de duas turmas. 
Cada turma tem 3 alunos. Armazene os dados em uma matriz M. 
Cada aluno deve ter três notas (as duas digitadas e a média dessas duas). 
Calcule a média de cada turma e armazene em um vetor TURMA. 
Informe qual turma tem maior média, e quais alunos tiveram média maior que a média de sua turma.
"""

alunos=3
notas=2
turmas=2
M=[]
mediaTurmas=[]
mediaAlunos=[]
for i in range(turmas):
    vetAlunos=[]
    notaAlunos=[]
    somaNotasTurma=0
    for j in range(alunos):
        vetNotas=[]
        for k in range(notas):
            vetNotas.append(float(input(f"Insira a nota {[k]} do aluno {[j]} da turma {[i]}: ")))
        vetAlunos.append(vetNotas)
        notaAlunos.append(sum(vetNotas)/notas)
        somaNotasTurma+=sum(vetNotas)
    mediaAlunos.append(notaAlunos)
    mediaTurmas.append(somaNotasTurma/(alunos*notas))
    M.append(vetAlunos)
print(f"\nTurma com maior média: Turma{[mediaTurmas.index(max(mediaTurmas))]}\nMédia da turma: {max(mediaTurmas):.1f}")
print("\nAlunos com média acima da média da sua turma: \n")
for i in range(turmas):
    for j in range(alunos):
        if(mediaAlunos[i][j]>mediaTurmas[i]):
            print(f"Turma{[i]} | Aluno{[j]} = {mediaAlunos[i][j]}")
    
