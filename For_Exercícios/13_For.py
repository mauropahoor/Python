'''13) Um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número. Exemplo 6 é um número perfeito, pois 6 = 1 + 2 +3.'''

n = int(input())
test = 0

for i in range(1, n):
    if(n % i == 0):
        test += i
if(test == n):
    print("Perfeito")
else:
    print("nao perfeito")
