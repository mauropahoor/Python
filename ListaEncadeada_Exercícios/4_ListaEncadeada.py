"""
1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem que os elementos foram digitados.
LSEC --> lista simplesmente encadeada circular
LDEC --> lista duplamente encadeada circular
LSED --> lista simplesmente encadeada com descritor
LDED --> lista duplamente encadeada com descritor
LSECD --> lista simplesmente encadeada circular com descritor
LDECD --> lista duplamente encadeada circular com descritor
"""
#Com LDED

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None
class LDED:
    def __init__(self):
        self.inicio = None
        self.fim = self.inicio
        self.quant = 0    
    def criarLDED(self):
        n = int(input("Digite o valor a ser inserido:\n"))
        while(n >= 0):
            self.inserir(n)
            n = int(input("Digite o valor a ser inserido:\n"))
    def inserir(self,valor):
        self.quant += 1
        if(self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
        else:
            self.fim.prox = No(valor)
            self.fim.prox.ant = self.fim
            self.fim = self.fim.prox
    def print(self):
        aux = self.inicio
        while(aux != self.fim):
            print(aux.valor)
            aux = aux.prox
        print(aux.valor)
        print("Quantidade de nodes", self.quant)

lista = LDED()
lista.criarLDED()
lista.print()