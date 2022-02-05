"""
8. Dado um vetor de 100 elementos, determine a diferença entre a soma dos elementos de índice par e a soma dos elementos de índice ímpar.
"""
tam = 5
vet = []
par = 0
impar = 0

for i in range(tam):
    vet.append(int(input("insira numero")))
    if(i % 2 == 0):
        par += vet[i]
    else:
        impar += vet[i]
print(par - impar)