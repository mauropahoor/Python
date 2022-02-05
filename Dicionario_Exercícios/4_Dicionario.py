"""
4. Foi feita uma estatística nas 200 principais cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
    •Nome da cidade
    •Estado (RJ, SC, PR, SP, RS, ...)
    •Número de veículos de passeio
    •Número de acidentes de trânsito com vítimas
Todos os dados foram armazenados em um dicionário, onde a chave é um número inteiro.
Deseja-se saber:
    a) Qual o maior e menor índice de acidentes de trânsito e a que cidade pertencem
    b) Qual a média de veículos nas cidades brasileiras
    c) Qual a média de acidentes com vítimas entre as cidades do Rio Grande do Sul
"""

information = {}
n = 1
tam = 200
while(n != tam + 1):
    info_city = {'name':input("Nome da city "), 'state':input("Estado "), 'veh_travel':input("Veiculos de passeio "), 'accidents': input("Acidentes de transitos ")}
    information[n] = info_city
    n += 1
max = -1
min = int(information[1]['accidents'])
med_veh = 0
med_accidents_rs = 0
city_rs = 0
owner_city_max = ""
owner_city_min = information[1]['name']
for tupla in information.items():
    if(int(tupla[1]['accidents']) > max):
        max = int(tupla[1]['accidents'])
        owner_city_max = tupla[1]['name']
    elif(int(tupla[1]['accidents']) < min):
        min = int(tupla[1]['accidents'])
        owner_city_min = tupla[1]['name']
    if(tupla[1]['state'].upper() == 'RS'):
        city_rs += 1
        med_accidents_rs += int(tupla[1]['accidents'])
    med_veh += int(tupla[1]['veh_travel'])
med_veh //= tam
print(f"""\n          O maior índice de acidentes pertence a cidade {owner_city_max} com {max} acidentes.\n
          O menor índice de acidentes pertence a cidade {owner_city_min} com {min} acidentes.\n
          A média de veículos nas cidades é de {med_veh} veículos.""")
if (city_rs == 0):
    print("A média de acidentes no Rio Grande do Sul é de 0 acidentes")          
else:
    med_accidents_rs //= city_rs
    print(f"A média de acidentes no Rio Grande do Sul é de {med_accidents_rs} acidentes.")
    