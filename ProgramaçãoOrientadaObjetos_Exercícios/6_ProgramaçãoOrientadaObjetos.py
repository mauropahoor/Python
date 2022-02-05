"""
6.Crie uma classe Aluno, que possui como atributo um nome e cpf. 
Crie outra classe chamada Equipe, que possui como atributo uma lista de participantes do tipo Aluno e outro atributo chamado projeto. 
A classe Equipe deve possuir um método para mostrar todos os alunos da equipe.
"""

class aluno:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
class equipe(aluno):
    def getAluno(self):
        return self.nome + '\n' + self.cpf
    def projeto(self):
        return 'Projeto'