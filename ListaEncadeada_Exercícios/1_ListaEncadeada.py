"""
1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem que os elementos foram digitados.
LSEC --> lista simplesmente encadeada circular
LDEC --> lista duplamente encadeada circular
LSED --> lista simplesmente encadeada com descritor
LDED --> lista duplamente encadeada com descritor
LSECD --> lista simplesmente encadeada circular com descritor
LDECD --> lista duplamente encadeada circular com descritor
"""
#Com LSEC

class No:
    def __init__(self, valor):
        self.prox = None
        self.valor = valor
class ListaEncadeadaCircular:
    def __init__(self):
        self.inicio = None
    def ultimoValor(self):
        aux = self.inicio
        while(aux.prox != self.inicio):
            aux = aux.prox
        return aux
    def inserir(self,valor):
        if(self.inicio == None):
            self.inicio = No(valor)
            self.inicio.prox = self.inicio
        else:
            end = self.ultimoValor()
            end.prox = No(valor)
            end.prox.prox = self.inicio
    def print(self):
        aux = self.inicio
        while(aux.prox != self.inicio):
            print(aux.valor)
            aux = aux.prox
        print(aux.valor)
    def criarLSEC(self):
        print("Digite o valor a ser inserido:")
        n = int(input(""))
        while (n >= 0):
            self.inserir(n)
            print("Digite o valor a ser inserido:")
            n = int(input(""))
lista = ListaEncadeadaCircular()
lista.criarLSEC()
lista.print()