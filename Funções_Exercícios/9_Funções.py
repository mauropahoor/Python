"""
9. Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou retângulo, calcule a área e o perímetro da figura•O programa deve primeiro perguntar qual o tipo da figura:
–(1) circunferência
–(2) triângulo
–(3) retângulo
•Dependendo do tipo de figura, ler o 
(1) tamanho do raio da circunferência; 
(2) tamanho de cada um dos lados do triângulo; 
(3) tamanho dos dois lados retângulo
•Usar funções sempre que possível
"""

def perimetro_circunferencia(r):
    return 2*3*r
def area_circunferencia(r):
    return 3*(r^2)
def perimetro_triangulo(l1, l2, l3):
    return l1+l2+l3
def area_retangulo(b, h):
    return b*h
def perimetro_retangulo(b, h):
    return (b+h) * 2

while (True):
    option = int(input("""
Digite a figura geométrica desejada:\n
–(1) circunferência\n
–(2) triângulo\n
–(3) retângulo\n"""))
    if(option == 1):
        r = int(input("Digite o raio da circunferencia. "))
        print("O perimetro é", perimetro_circunferencia(r),"\n","A area é", area_circunferencia(r))
    elif(option == 2):
        l1 = int(input("Digite o l1 do triangulo. "))
        l2 = int(input("Digite o l2 do triangulo. "))
        l3 = int(input("Digite o l3 do triangulo. "))
        print("O perimetro é", perimetro_triangulo(l1, l2, l3))
    elif(option == 3):
        b = int(input("Digite a base do retangulo. "))
        h = int(input("Digite a altura do retangulo. "))   
        print("O perimetro é", perimetro_retangulo(b, h), "\n","A area é", area_retangulo(b, h))
    else:
        print("Opção invalida.")