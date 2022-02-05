''''''

n = int(input("Insira o numero:"))
j = n
tamN = len(str(n))
aux = 0

for i in range(tamN):
    aux += (n % 10) ** tamN
    n //= 10
if(aux == j):
    print(f"{j} é um numero Armstrong")
else:
    print(f"{j} não é um numero Armstrong")