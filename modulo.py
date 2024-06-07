from datetime import date

#função menu
def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{dia} de {meses[mes - 1]} de {ano}.\n')
    print('1 - Calcular quadrilatero')
    print('2 - Calcular circulo')
    print('3 - Calcular triangulo')
    print('4 - Calcular trapézio')
    print('5 - Sair do programa')

#função do quadrilatero
def calcular_quadrilatero(b, h):
    a = b * h
    return a

#função do circunferencia
def calcular_circulo(r):
    a = 3.14*r**2
    return a

#função do triangulo
def calcular_triangulo(b, h):
    a = (b * h)/2
    return a

#função do trapézio
def calcular_trapézio(b_menor, b_maior, h):
    a = ((b_menor + b_maior)*h)/2
    return a

