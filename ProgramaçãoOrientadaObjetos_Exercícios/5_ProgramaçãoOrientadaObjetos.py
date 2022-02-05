"""
5. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    •Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    •O consumo é especificado no construtor e o nível de combustível inicial é 0.
    •Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina. Esse método recebe como parâmetro a distância em km.
    •Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    •Forneça um método adicionarGasolina( ), para abastecer o tanque.
    •Faça um programa para testar a classe Carro. Exemplo de uso:
        meuFusca= Carro(15);  # 15 quilômetros por litro de combustível.
        meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
        meuFusca.andar(100); # anda 100 quilômetros.
        meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
"""

class carro:
    def __init__(self,consumo):
        self.__consumo = consumo
        self.combustivel = 0
    def obter_gasolina(self):
        return self.combustivel
    def adicionar_gasolina(self,v):
        self.combustivel += v
        return self.combustivel
    def andar(self,v):
        self.combustivel -= v/self.__consumo
        return self.combustivel
    
celta = carro(10)
while True:
    opt = input("Digite a funcao que deseja usar\n1 -- Consultar gasolina\n2 -- Adicionar gasolina\n3 -- Andar ")
    if (opt == '1'):
        print("A quantidade de gasolina no tanque é",celta.obter_gasolina())
    elif (opt == '2'):
        a = int(input("Digite o valor de gasolina para adicionar: "))
        celta.adicionar_gasolina(a)
    elif (opt == '3'):
        a = int(input("Digite a distancia a ser percorrida: "))
        celta.andar(a)