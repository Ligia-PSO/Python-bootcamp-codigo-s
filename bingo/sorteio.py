"""Módulo para gerar números aleatórios"""
import cartela
from random import choice,randint,seed
seed()#go back to random generation invalidating seed(1) specified on cartela.py
def sorteia():
    """Sorteia um número para o bingo."""
    
    letra_sorteada = choice(cartela.LETRAS)
    # letra_sorteada = "G"

    minimo, maximo = cartela.min_max(letra_sorteada)

    numero_sorteado = randint(minimo, maximo)
    # numero_sorteado = 60

    print(f"A combinação sorteada foi {letra_sorteada}{numero_sorteado}")

    return letra_sorteada, numero_sorteado
