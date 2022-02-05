"""
4. Faça uma função que receba um caractere retorne Truese for vogal e False caso contrário
"""
def vog(x):
    if(x in "aeiou"):
        return True
    else:
        return False
n = input()
if(vog(n)):
    print("Vogal")
else:
    print("Nao vogal")