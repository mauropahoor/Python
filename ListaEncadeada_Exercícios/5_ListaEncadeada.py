"""
1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem que os elementos foram digitados.
LSEC --> lista simplesmente encadeada circular
LDEC --> lista duplamente encadeada circular
LSED --> lista simplesmente encadeada com descritor
LDED --> lista duplamente encadeada com descritor
LSECD --> lista simplesmente encadeada circular com descritor
LDECD --> lista duplamente encadeada circular com descritor
"""
#Com LSECD

class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None
class LSECD:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quant = 0
    def print(self):
        aux = self.inicio
        while(aux != self.fim):
            print(aux.valor)
            aux = aux.prox
        print(aux.valor)
        print("A quantidade de nodes é", self.quant)
    def criarLSECD(self):
        n = int(input("Digite o valor:\n"))
        while(n >= 0):
            self.inserir(n)
            n = int(input("Digite o valor:\n"))
    def inserir(self,valor):
        self.quant += 1
        if (self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
            self.fim.prox = self.inicio
        else:
            self.fim.prox = No(valor)
            self.fim = self.fim.prox
            self.fim.prox = self.inicio
lista = LSECD()
lista.criarLSECD()
lista.print()