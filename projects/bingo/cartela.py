"""Módulo com funções e variáveis para cartela de bingo."""

from collections import defaultdict
from random import randint, seed
from numpy import array,fliplr
# Travando a aleatoriedade da cartela
seed(1)#If you use the same seed value twice you will get the same random number twice

LETRAS = ("B", "I", "N", "G", "O")


def min_max(letra: str) -> tuple:
    """Gera o valor mínimo e máximo para a letra dada.

    Args:
        letra (str): Letra de input

    Returns:
        tuple[int]: valores mínimo e máximo
    """
    intervalo = {"B": (1, 15), "I": (16, 30), "N": (31, 45), "G": (46, 60), "O": (61, 75)}

    minimo, maximo = intervalo[letra][0], intervalo[letra][1]

    return minimo, maximo


# Passo número 0
def gerar() -> defaultdict():
    """Gera uma cartela com 5 números aleatórios para cada letra."""

    cartela = defaultdict(list)

    for letra in LETRAS:
        # Coletar o número mínimo e máximo de cada letra
        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5:
            # Gerar um número aleatório
            num_aleatorio = randint(minimo, maximo)

            # Verificar se o número não existe naquela letra
            if num_aleatorio in cartela[letra]:
                continue#volta para o inicio do loop ou seja para whle len(.... nesse caso

            # Colocar número aleatório na lista
            cartela[letra].append(num_aleatorio)

            # Ordena em ordem crescente os números
            cartela[letra].sort()

    return cartela


# Passo número 1:
def imprime(cartela: dict) -> None:
    """Formata a cartela para imprimir na tela

    Args:
        cartela (dict[str, list[int]]): cartela de entrada
    """

    print(" B   I   N   G   O")

    # Para cada linha ele imprime os elementos daquela linha na tela
    for linha in range(5):

        # Gera a lista de elementos já formatada
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]

        # Junta a lista de strings para impressão com uma `,`
        string = ", ".join(lista_str)

        print(string)


# Passo 2 (além!)
def marca_numero(cartela: defaultdict, letra: str, numero: int, caracter: str):
    # Coletar o índice da lista do número sorteado
    indice = cartela[letra].index(numero)

    cartela[letra][indice] = caracter

    return cartela


# Passo 2:
def numero_existe(cartela, letra, numero):
    if numero in cartela[letra]:
        # print("Você acertou um número!")
        return True
    # print("Você errou!")
    return False

def verify_bingo(cartela:dict)->bool:
    cartela_matrix=array(list(cartela.values()))

    #check bingo on diagonal
    if ["XX"]*5 in map(list,[cartela_matrix.diagonal(0),fliplr(cartela_matrix).diagonal(0)]):
        return True

    #check bingo on columns and rows
    for i in range(5):
        if ["XX"]*5 in map(list,[cartela_matrix[:,i],cartela_matrix[i,:]]):
            return True
    return False
