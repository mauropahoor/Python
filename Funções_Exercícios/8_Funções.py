"""
8-Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8
.Estado da memória: 0
Opções:(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
Qual opção você deseja?
"""
def soma(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a*b
def dividir(a, b):
    return a/b

em = 0 #Estado de memória
option = 0
while(option != 6):
    option = int(input(f"""Opções:\n
(1) Somar\n
(2) Subtrair\n
(3) Multiplicar\n
(4) Dividir\n
(5) Limpar memória\n
(6) Sair do programa\n
Qual opção você deseja?\n
Estado de memória = {em}\n"""))
    if(option == 1):
        b = int(input("Digite um numero para a soma "))
        print("\nO resultado é", soma(em, b))
        em = soma(em, b)
    elif(option == 2):
        b = int(input("Digite um numero para a subtraçao "))
        print("\nO resultado é", subtrair(em, b))
        em = subtrair(em, b)
    elif(option == 3):
        b = int(input("Digite um numero para a multiplicação "))
        print("\nO resultado é", multiplicar(em, b))
        em = multiplicar(em, b)
    elif(option == 4):
        b = int(input("Digite um numero para a divisão "))
        if(em == 0):
            print("A divisão não é possivel devido ao estado de memoria ser igual a 0, tente outra operação.")
        else:    
            print("\nO resultado é", dividir(em, b))
            em = dividir(em, b)
    elif(option == 5):
        em = 0
    else:
        print("Opção inválida.\n\n")
print("Programa encerrado.")
