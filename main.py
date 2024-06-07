#faz aas importações
import os
from modulo import *

#programa principal
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('opção desejada: ')
        os.system('cls')

        match opcao:
            case '1':
                b = int(input('Base do quadrilatero: '))
                h = int(input('Altura do quadrilatero: '))
                print(f'Area: {calcular_quadrilatero(b, h)}')
                continue
            case '2':
                r = int(input('Raio do circulo: '))
                print(f'Area: {calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Area: {calcular_triangulo(b, h)}')
                continue
            case '4':
                b_menor = int(input('Base menor do trapézio: '))
                b_maior = int(input('Base do maior do trapézio: '))
                h = int(input('Altura do trapézio: '))
                print(f'Area: {calcular_trapézio(b_menor, b_maior, h)}')
                continue
            case '5':
                break
            case _:
                print('Opção inválida.')
                continue