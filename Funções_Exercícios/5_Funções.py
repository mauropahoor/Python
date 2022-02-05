"""
5. Faça uma função que receba um caractere retorne Truese for consoante e False caso contrário
"""
def con(x):
    if(x in "qwrtypsdfghjklçzxcvbnm"):
        return True
    else:
        return False
n = input()
if(con(n)):
    print("Consoante")
else:
    print("Nao consoante")
