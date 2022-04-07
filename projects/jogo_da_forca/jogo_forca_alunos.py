"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.

Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from random import choice
from sre_parse import State
from utils import WORDS,STATUS

def get_secret_word()->str:
    """Devolve uma palavra aleatória de uma lista."""
    word_list=WORDS
    word=choice(word_list)
    return word

def print_game_board(  secret_word: str,
    correct_letters: list[str],
    missed_letters: list[str],
    error: int,
    attempts: int,
    status: list[str],
) -> None:
    """Imprime a situação atual do jogo.

    Args:
        secret_word (str): palavra secreta
        correct_letters (list[str]): lista de letras corretas já jogadas
        missed_letters (list[str]): lista de letras incorretas já jogadas
        error (int): número de erros cometidos
        attempts (int): tentantivas restantes
        status (list[str]): status do jogo
    """

    encoded_word = ""

    for letter in secret_word:
        if letter not in correct_letters:
            encoded_word += "_"
        else:
            encoded_word += letter

    if error <= attempts:
        print(status[error])

        print(encoded_word)

    print(f"\nLetras corretas: {' '.join(correct_letters)}")

    print(f"\n Letras erradas: {' '.join(missed_letters)}")

    return None #boa pratica colocar 

    """Imprime a situação atual do jogo."""

def read_input_player()->str:
    """Lê uma letra do usuário."""
    
    letter=input("\nguess a letter: ").upper()
    while len(input_char) != 1:
        print("Entre com apenas um caracter!")
        input_char = input("\nDigite uma letra com um único caracter: ").upper()
    return input_char

    return letter



def guess_letter(secret_word:str,input_char:str,correct_letters:list,wrong_letters:list)->bool:
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""

    if input_char in correct_letters or input_char in wrong_letters:
        print(f"a letra {input_char} ja foi jogada escolha outra")
        return False
    
    elif input_char in secret_word:
        correct_letters.append(input_char)
        return True
    else: 
        wrong_letters.append(input_char)
        return False

def game_continue(correct_letters:str, secret_word:str, error:int, attempts:int, STATUS:str)->bool:
    if error>=attempts :
        print(STATUS[error])
        print(f"A palavra secreta é {secret_word}")
        return False
    elif set(correct_letters)==set(secret_word):
        print(STATUS[error])
        print("Voce ganhou!!!")
        return False
    return True

"""Função que decide se jogo já encerrou ou não."""
    


secret_word = get_secret_word()
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadasa
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue(correct_letters, secret_word, error, attempts, STATUS):
    print_game_board(secret_word, correct_letters, missed_letters, error, attempts, STATUS)
    input_char=read_input_player()
    if not  guess_letter(secret_word,input_char,correct_letters,missed_letters):
        error+=1
