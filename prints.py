from os import system
from time import sleep

def printNoLargura(estado, noExpandido):
        system('cls')
        estado = eval(estado)
        print("Usando Busca em Largura:\n")
        print("  Nós Expandidos: %d\n" %(noExpandido))
        print('      ',estado[0][0], estado[0][1], estado[0][2])
        print('      ',estado[1][0], estado[1][1], estado[1][2])
        print('      ',estado[2][0], estado[2][1], estado[2][2])
        print("\n")
        sleep(0.5)

def printNoProfundidade(estado, noExpandido):
        system('cls')
        estado = eval(estado)
        print("Usando Busca em Profundidade Limitada Iterativa:\n")
        print("  Nós Expandidos: %d\n" %(noExpandido))
        print('      ',estado[0][0], estado[0][1], estado[0][2])
        print('      ',estado[1][0], estado[1][1], estado[1][2])
        print('      ',estado[2][0], estado[2][1], estado[2][2])
        print("\n")
        sleep(0.5)