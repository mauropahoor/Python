"""
6. O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. 
Faça o programa que lê o valor de N e M e informa o número de combinações possíveis
–Número de combinações é igual a N!/(M! * (N-M)!)
–Use funções para evitar repetição de código
"""
def combinacoesPossiveis(a, b):
    fat_a = 1
    fat_b = 1
    fat_ab = 1 #Fatorial de a-b
    for i in range(2 , a + 1):
        fat_a *= i
    for i in range(2 , b + 1):
        fat_b *= i
    for i in range(2 , (a - b) + 1):
        fat_ab *= i
    result = fat_a/(fat_b * fat_ab)
    return result
n = int(input("Digite a primeira turma "))
m = int(input("Digite a segunda turma "))

print("O número de combinações possiveis é de", combinacoesPossiveis(n, m))
        
