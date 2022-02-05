'''
17)Diga quantas vezes a senteçaS será executada.
for j in range(1, 11):
    for l in range(1, j+1):
        S'''

S = 0

for j in range(1, 11):
    for l in range(1, j+1):
        S += 1
print(S)