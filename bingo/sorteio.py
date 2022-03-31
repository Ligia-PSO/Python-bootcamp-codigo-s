"""Módulo para gerar números aleatórios"""
import cartela
import numpy as np
import copy
from random import choice,randint,seed
from termcolor import colored

def sorteia():
    seed()
    """Sorteia um número para o bingo."""
    
    letra_sorteada = choice(cartela.LETRAS)
    # letra_sorteada = "G"

    minimo, maximo = cartela.min_max(letra_sorteada)

    numero_sorteado = randint(minimo, maximo)
    # numero_sorteado = 60

    # print(f"A combinação sorteada foi {letra_sorteada}{numero_sorteado}")

    return letra_sorteada, numero_sorteado


def run_bingo(cartela_input:dict(),number_of_sorts:int or None=None)->int or None:
# returns number of sorteios necessarios
    cartela_1=copy.deepcopy(cartela_input)#need to use deepcopy becuse i dontwant them to point to the same value just a second copy dictionary
    cartela_show=copy.deepcopy(cartela_input)
   
    if number_of_sorts==None:
        num_draws=0
        while cartela.verify_bingo(cartela_1)==False:
            letra_sorteada, numero_sorteado = sorteia()
            # letra_sorteada, numero_sorteado="N",36
            if cartela.numero_existe(cartela_1, letra_sorteada, numero_sorteado):
                cartela_1= cartela.marca_numero(cartela_1, letra_sorteada, numero_sorteado, "XX")

            num_draws+=1        

        # cartela.imprime(cartela_show)
        return num_draws #number of draws until a bingo occurence
    else:
        for _ in range(number_of_sorts):
            letra_sorteada, numero_sorteado = sorteia()
            # letra_sorteada, numero_sorteado="N",36
            if cartela.numero_existe(cartela_1, letra_sorteada, numero_sorteado):
                #cartela_show->Special dictionary just for a more visually apealing print of the cartela marked with colors
                cartela_show = cartela.marca_numero(cartela_show, letra_sorteada, numero_sorteado, colored(str(numero_sorteado).zfill(2), 'yellow'))
                cartela_1= cartela.marca_numero(cartela_1, letra_sorteada, numero_sorteado, "XX")
        cartela.imprime(cartela_show)

        if cartela.verify_bingo(cartela_1):
            print(f"\nBINGO com {number_of_sorts} sorteios")
            return()

        print(f"\nNao foi possivel obter BINGO com {number_of_sorts} sorteios")
        return()
