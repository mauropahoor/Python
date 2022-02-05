"""
4. Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir(em horas). 
Essa classe deverá ter os seguintes métodos:
    –estudar (que recebe como parâmetro a qtdde horas de estudo e acrescenta tempoSemDormir)
    –Dormir (que recebe como parâmetro a qtdde horas de sono e reduz tempoSemDormir)
Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir. 
Ao final imprima quanto tempo o aluno está sem dormir
"""

class aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    def estudar(self,v):
        self.tempoSemDormir += v
        return self.tempoSemDormir
    def dormir(self,v):
        self.tempoSemDormir -= v
        return self.tempoSemDormir
    def getTemposemdormir(self):
        return self.tempoSemDormir
    
a1 = aluno('Mauro','Informatica',0)
while True:
    opt = input("Digite a funcao que deseja usar\n1 -- Adicionar horas estudadas\n2 -- Adicionar horas dormidas: ")
    if (opt == '1'):
        a = int(input("Digite o tempo estudado: "))
        a1.estudar(a)
    elif (opt == '2'):
        a = int(input("Digite o tempo dormido: "))
        a1.dormir(a)
    else:
        print("Opcao Invalida.")
    print("O tempo sem dormir é",a1.getTemposemdormir(),"horas")