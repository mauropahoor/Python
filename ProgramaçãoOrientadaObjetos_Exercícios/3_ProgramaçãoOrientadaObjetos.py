"""
3.Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
    –Crie os métodos getPrecopara obter o valor do preco e o método setPrecopara setar um novo valor do preco.
Crie um código de teste.
"""

class livro:
    def __init__(self,nome,qtdPaginas,autor,preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    def setPreco(self, v):
        self.preco = v

nome = input("Digite o nome do livro: ")
qtdPaginas = input("Digite a quantidade de paginas: ")
autor = input("Digite o autor")
preco = input("Digite o preco")
l1 = livro(nome,qtdPaginas,autor,preco)

while True:
    opt = input("Digite o que deseja consultar\n1 -- Conferir o preço\n2 -- Alterar o preco: ")
    if (opt == '1'):
        print("O preço do livro é",l1.getPreco())
    elif (opt == '2'):
        n = int(input("Digite o novo preco do livro: "))
        l1.setPreco(n)
        print("O novo preco é", l1.getPreco())