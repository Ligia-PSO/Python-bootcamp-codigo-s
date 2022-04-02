"""
Lista de exercicios
Tema: funcoes
"""


"""================================================Exercicio 1:========================================================================
Em uma determinada pais, as tarifas de taxi consistem em uma tarifa basica de R$4,00 mais R$0,25 para cada 140 metros percorridos.
 Escreva uma funcao que receba a distancia percorrida (em quilometros) como unico parametro e retorna a tarifa total como unico resultado.
  Escreva um programa que demonstre o uso da sua funcao.
"""
def ex1():
    distance_covered=int(input("Distancia percorrida: "))
    tax=4+distance_covered//140*0.25
    print(f"a tarifa foi de: R${tax}")
    
# ex1()

"""================================================Exercicio 2:========================================================================
Escreva uma funcao que, dado tres comprimentos de retas quaisquer, diga se essas tres retas podem ou nao formar um triangulo, retornando true em caso positivo e false em caso negativo
Dica ndeg1: Se algum dos comprimentos for negativo ou zero, nao e possivel formar um triangulo.
Dica ndeg2: se qualquer um dos comprimentos for maior ou igual a soma dos outros dois, entao os comprimentos nao podem ser usados para formar um triangulo. 
Caso contrario, eles podem formar um triangulo.
"""
def ex2():
    a,b,c=map(int,input("forneça os tres lados do triangulo:").split(","))
    if min(a,b,c)<=0:
        return(print(False))
    if a>=b+c or b>a+c or c>b+c:
        return(print(False))
    return(print(True))
# ex2()


"""================================================Exercicio 3:========================================================================
Faca uma funcao que retorne o reverso de um numero inteiro informado. Por exemplo: 127 -> 721.
"""
def ex3():
    number=int(input("forneça um numero inteiro: "))
    number=str(number)[::-1]
    print(int(number))
# ex3()


"""================================================Exercicio 4:========================================================================
Embaralha palavras: Construa uma funcao que receba uma string como parametro e devolva outra string com os carateres embaralhados. 
Por exemplo: se funcao receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinacao possivel, de forma aleatoria.
 Padronize em sua funcao que todos os caracteres serao devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
from random import choice
from xml.dom.minicompat import StringTypes
def ex4():
    string_list=[letter for letter in input("Digite uma string: ")]
    string_out=""
    for _ in range(len(string_list)):
        random_letter=choice(string_list)
        string_out+=random_letter
        string_list.remove(random_letter)
    print(string_out)
# ex4()

"""================================================Exercicio 5 (desafio):========================================================================
Quadrado magico: Um quadrado magico e aquele dividido em linhas e colunas, com um numero em cada posicao e no qual a soma das linhas, colunas e diagonais e a mesma. 
Por exemplo, veja um quadrado magico de lado 3, com numeros de 1 a 9:
8  3  4 
1  5  9
6  7  2
Elabore uma funcao que identifica e mostra na tela todos os quadrados magicos com as caracteristicas acima.
 Dica: produza todas as combinacoes possiveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""
import numpy as np
from itertools import permutations

def verify_magic_square(square:np.ndarray)->bool:
    column_list=[square[:,i] for i in range(3)]
    row_list=[square[i,:] for i in range(3)]
    diagonals=[square.diagonal(0),np.fliplr(square).diagonal(0)]
    column_list.extend(row_list)
    column_list.extend(diagonals)

    if all([sum(lista)==15 for lista in column_list]):
        return(True)
    return(False)

def generate_squares():

    print("\n===========| Prining all possible magical squares |===========")
    possible_squares=[i for i in  range(1,10)]# possible magic squares
    square_list=list(map(list,permutations(possible_squares)))

    for number_list in square_list:
        square=np.array(np.array_split(number_list,3))

        if verify_magic_square(square):
            print('\n'.join(['  '.join([str(cell) for cell in row]) for row in square]))
            print("\n")

    print("===========================| END |===========================")
    
generate_squares()
