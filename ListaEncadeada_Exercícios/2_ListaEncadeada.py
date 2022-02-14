"""
1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem que os elementos foram digitados.
LSEC --> lista simplesmente encadeada circular
LDEC --> lista duplamente encadeada circular
LSED --> lista simplesmente encadeada com descritor
LDED --> lista duplamente encadeada com descritor
LSECD --> lista simplesmente encadeada circular com descritor
LDECD --> lista duplamente encadeada circular com descritor
"""
#Com LDEC

class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None
        self.ant = None
class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None
    def ultimoValor(self):
        aux = self.inicio
        while(aux.prox != self.inicio):
            aux = aux.prox
        return aux
    def print(self):
        aux = self.inicio
        while(aux.prox != self.inicio):
            print(aux.valor)
            aux = aux.prox
        print(aux.valor)
    def inserir(self,valor):
        if(self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
            self.inicio.prox = self.fim
            self.fim.prox = self.inicio
            self.inicio.ant = self.fim
        else:
            end = self.ultimoValor()
            end.prox = No(valor)
            end.prox.ant = end
            end = end.prox
            end.prox = self.inicio
    def criarLDEC(self):
        n = int(input("Digite o valor a ser inserido na LDEC:\n"))
        while(n >= 0):
            self.inserir(n)
            n = n = int(input("Digite o valor a ser inserido na LDEC:\n"))
lista = ListaDuplamenteEncadeadaCircular()
lista.criarLDEC()
lista.print()