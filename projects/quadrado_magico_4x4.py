"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.

Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""
import numpy as np
from itertools import permutations


def verify_magic_square(square:np.ndarray,sum_s:int)->bool:
    column_list=[square[:,i] for i in range(len(square))]
    row_list=[square[i,:] for i in range(len(square))]
    diagonals=[square.diagonal(0),np.fliplr(square).diagonal(0)]
    column_list.extend(row_list)
    column_list.extend(diagonals)

    if all([sum(lista)==sum_s for lista in column_list]):
        return(True)
    return(False)
# 
def generate_squares():

    square_size=int(input("diga o tamanho do quadrado:"))
    sum_square=square_size*((square_size**2+1))/2

    print("\n===========| Prining all possible magical squares |===========")

    number_list=[i for i in  range(1,square_size**2+1)]# List of numbers to be used

    square_list=list(map(list,permutations(number_list)))

    for number_list in square_list:
        square=np.array(np.array_split(number_list,square_size))

        if verify_magic_square(square,sum_square):
            print('\n'.join(['  '.join([str(cell) for cell in row]) for row in square]))
            print("\n")

    print("===========================| END |===========================")
    
# Sem dicas agora! Tentem elaborar toda a lógica do zero!
