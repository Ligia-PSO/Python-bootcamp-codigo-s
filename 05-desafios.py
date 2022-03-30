""""""
"""================================================Desafios!========================================================================
Onde o filho chora e a mae nao ve! Muahahahahaha...
(Brincadeiras a parte, todos voces serao capazes! Cada um no seu tempo!)
"""
"""================================================Desafio 1:========================================================================
Implemente um jogo em que o usuario tenha que adivinhar um numero sorteado pelo computador.
O jogo deve sortear um numero entre 1 e 100.
O usuario deve informar um numero. O numero informado pelo usuario deve ser validado: nao pode ser inferior a 1 ou superior a 100. Enquanto o usuario informar um numero invalido, o jogo deve solicitar a entrada de um novo numero.
O numero do usuario deve ser analisado:
Caso o usuario informe um numero inferior ao numero sorteado, o jogo deve apresentar a mensagem "O numero sorteado e maior.".
Caso o usuario informe um numero superior ao numero sorteado, o jogo deve apresentar a mensagem "O numero sorteado e menor.".
Caso o usuario informe um numero igual ao numero sorteado, o jogo deve apresentar a mensagem "Parabens! Voce acertou o numero sorteado" e o jogo deve ser finalizado, sendo apresentado ao usuario a quantidade de tentativas efetuadas ate este momento.
Ao final do jogo, deve-se questionar o usuario se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrario, o jogo deve ser encerrado.
Dica!
Pesquise sobre o modulo buit-in do Python chamado random
"""
# from random import seed


from unittest import skip


def desafio1():
    numero=int(input("Sugira um numero:"))
    # random_num=seed(10)

    print(numero)


# desafio1()

"""================================================Desafio 2:========================================================================
Implemente um jogo em que o usuario tenha que adivinhar o somatorio de dois dados.
O jogo deve sortear um numero para cada dado. Estes numeros devem variar entre 1 e 6, inclusive. Deve-se calcular a soma dos dois valores.
O usuario deve informar um numero. O numero informado pelo usuario deve ser validado: nao pode ser inferior a 2 ou superior a 12. Enquanto o usuario informar um numero invalido, o jogo deve solicitar a entrada de um novo numero.
O numero do usuario deve ser analisado e o resultado da jogada deve ser apresentado na tela:
Caso o usuario informe um numero superior ou inferior a soma dos dados, o jogo deve apresentar a mensagem "Voce errou. A soma dos dados e x. 
O valor do primeiro dado e d1 e o do segundo e d2. ", sendo x o valor da soma, d1 o valor do primeiro dado e d2 o valor do segundo dado.
Caso o usuario informe um numero igual ao valor da soma, o jogo deve apresentar a mensagem "Parabens! Voce acertou a soma dos dados! O valor do primeiro dado e d1 e o do segundo e d2. ", sendo d1 o valor do primeiro dado e d2 o valor do segundo dado
Ao final do jogo, deve-se questionar o usuario se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrario, o jogo deve ser encerrado.
"""


"""================================================Exercicio 3:========================================================================
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra.
Dada uma string qualquer, desenvolva um algoritmo que encontre o numero de pares de substrings que sao anagramas.
O que sao anagramas? https://pt.wikipedia.org/wiki/Anagrama
Bom divertimento!
"""
def ex3():
    first_word=input("digite a primeira palavra:")
    second_word=input("digite a segunda palavra:")
    for letter in first_word:
        if letter in second_word:
            if letter==first_word[-1]:
                print("as duas palavras sao anagramas")
        else:
            print("os dois pares de palavras dados nao sao anagramas um do outro")
            break
    
ex3()