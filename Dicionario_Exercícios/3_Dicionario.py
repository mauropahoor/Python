"""
3. Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. 
Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.
"""

dados = {}
dados_nounder18 = {}
n = True
while(n):
    agenda = {'nome':input("Nome "), 'idade':input("Idade "), 'cpf':input("CPF ")}
    dados[agenda['nome']] = agenda
    n = input("Deseja adicionar mais CPF's? [0/1] ")
    if(n == '0'):
        n = False
for tupla in dados.items():
    if(int(tupla[1]['idade']) >= 18):
        dados_nounder18[tupla[1]['nome']] = tupla[1]
while(True):
    name = input("Digite o nome que deseja buscar ")
    print(dados_nounder18.get(name))