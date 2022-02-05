'''
18)Reescreva o trecho abaixo utilizando while.
for j in range(1, 11):
    for l in range(1, j+1):
        S'''

j = 1
l = 1
S = 0
while(j != 11):
    l = 1
    while(l != j+1):

        S+=1
        l +=1
    j += 1
print(S)