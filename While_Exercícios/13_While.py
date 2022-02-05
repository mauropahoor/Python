'''
13) Um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número.
Exemplo 6 é um número perfeito, pois 6 = 1 + 2 +3.'''

n = int(input())
perfCheck = 0
i = 1

while(i <= n):
    if(n % i == 0 and (n // i) != 1):
        perfCheck += i
    i += 1
if(perfCheck == n):
    print(f"O número {n} é perfeito")
else:
    print(f"O número {n} não é perfeito")
