"""
3.Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. 
Caso o valor x não seja encontrado, o programa deve imprimir o valor -1.  
Faça a questão de duas formas: não utililizandoo método index() e utilizando o método index().
"""
#%%
tam = 5
vet = [0] * tam

for i in range(len(vet)):
    vet[i] = input(f"Digite o valor {i + 1} do vetor:\n")
x = input("Digite o valor a ser encontrado:\n")
print(vet.index(x))

#%%
tam = 5
vet = [0] * tam
end = 0

for i in range(len(vet)):
    vet[i] = input(f"2Digite o valor {i + 1} do vetor:\n")
x = input("Digite o valor a ser encontrado:\n")
for i in range(len(vet)):
    if(vet[i] == x):
        print(f"X está na posição {i + 1}")
        end += 1
if(end == 0):
    print(-1)
