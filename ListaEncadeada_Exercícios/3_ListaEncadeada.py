"""
1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem que os elementos foram digitados.
LSEC --> lista simplesmente encadeada circular
LDEC --> lista duplamente encadeada circular
LSED --> lista simplesmente encadeada com descritor
LDED --> lista duplamente encadeada com descritor
LSECD --> lista simplesmente encadeada circular com descritor
LDECD --> lista duplamente encadeada circular com descritor
"""
#Com LSED

class No:
    def __init__(self,valor):
        self.prox = None
        self.valor = valor
class ListaSimplesmenteEncadeadaComDescritor:
    def __init__(self):
        self.inicio = None
        self.quantidadeNo = 0
        self.fim = None
    def print(self):
        aux = self.inicio
        while(aux != self.fim):
            print(aux.valor)
            aux = aux.prox
        print(aux.valor)
        print("A quantidade de Nodes é de", self.quantidadeNo)
    def criarLSED(self):
        n = int(input("Digite o valor a ser inserido:\n"))
        while(n >= 0):
            self.inserir(n)
            n = int(input("Digite o valor a ser inserido\n"))
    def inserir(self,valor):
        self.quantidadeNo += 1
        if(self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
        else:
            self.fim.prox = No(valor)
            self.fim = self.fim.prox
lista = ListaSimplesmenteEncadeadaComDescritor()
lista.criarLSED()
lista.print()
        