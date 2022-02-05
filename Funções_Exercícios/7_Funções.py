"""
7. Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
–Nota acima de 6  “Aprovado”
–Nota entre 4 e 6  “Verificação Suplementar”
–Nota abaixo de 4  “Reprovado”. 
"""

def med(x):
    if(x >= 6):
        return "Aprovado"
    elif (x < 6 and x >= 4):
        return "Verificação Suplementar"
    else:
        return "Reprovado"

n = int(input("Digite a sua média "))

print(med(n))

