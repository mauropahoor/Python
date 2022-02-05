"""Reescreva os 7 métodos para implementação de LSE, vistos em aula, com recursão.  
(2. mostrar LSE na tela;)."""
#Algoritmos Computacionais e Estruturas de Dados
#Lista Simplesmente Encadeada em Python
#Prof.: Laercio Brito
#Dia: 28/01/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 2

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        
    def return_start(self):
        return self.inicio
    
    def print_list(self, aux):
        if (aux != None):
            print(aux.valor)
            aux = aux.prox
            self.print_list(aux)
        else:
            return print('Programa Finalizado.')
        
    def inserir(self, valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux
        
    def criarLSEInversa(self):
        valor = int(input("Digite o valor: "))
        if(valor <= 0):
            return 0
        else:
            self.inserir(valor)
            lista.criarLSEInversa()

lista = ListaEncadeada()
lista.criarLSEInversa()
lista.print_list(lista.return_start())