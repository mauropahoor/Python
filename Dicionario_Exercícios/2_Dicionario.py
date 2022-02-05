"""
2.Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone. 
O programa deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: 
    nome-idade-fone
"""

n = True
dados = {}

while(n):
    agenda = {'cpf':input("CPF "), 'nome':input("Nome "), 'idade':input("Idade "), 'fone':input("Tel ")}
    dados[agenda['cpf']] = agenda
    n = input("Deseja adicionar mais CPF's? [0/1]")
    if(n == '0'):
        n = False
for tupla in dados.items():
    print(f"\n{tupla[0]}: {tupla[1]['nome']} {tupla[1]['idade']} {tupla[1]['fone']}")