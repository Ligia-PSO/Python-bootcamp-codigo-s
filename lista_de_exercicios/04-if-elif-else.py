"""Lista de exercicios
Tema: condicionais
Diversao do carnaval \o/
"""
"""================================================Exercicio 1:========================================================================
Escreva um programa que diga se um numero dado pelo usuario e par ou impar
"""
from pickle import FALSE


def ex1():
    number=int(input("dingite um numero: "))
    if number%2==0:
        print("o numero{number} e par")
    else:
        print("o numero{number} e impar")
# ex1()

"""================================================Exercicio 2:========================================================================
Escreva um programa que receba dois numeros e imprima na tela se o primeiro e divisivel pelo segundo.
"""
def ex2():
    number_1=int(input("dingite o primeiro numero: "))
    number_2=int(input("dingite o segundo numero: "))
    if number_1%number_2==0:
        print(f"o numero{number_1} e divisivel por {number_2} ")
    else:
        print(f"o numero{number_1} nao e divisivel por {number_2} ")
# ex2()

"""================================================Exercicio 3:========================================================================
A tabela a seguir lista os niveis sonoros em decibeis para alguns barulhos comuns
Barulho
Nivel sonoro (dB)
Britadeira
130
Cortador de grama
106
Despertador
70
Comodo em silencio
40
Escreva um programa que leia um valor de nivel sonoro do usuario em decibeis. Se o valor for um dos que estao na tabela, o programa deve retornar aquele barulho.
 Caso o numero esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado esta. 
 Seu programa deve informar tambem quando o valor for menor que o ruido minimo da tabela e maior que ruido maximo. 
"""
def ex5():
    sounds={
        "Britadeira":130,
        "Cortador de grama":106,
        "Despertador":70,
        "Comodo em silencio":40
    }
    input_sound_level=int((input("Sound level:")))
    
    if input_sound_level in sounds.values():

        return(print(f"{list(sounds.keys())[list(sounds.values()).index(input_sound_level)]} : {input_sound_level}"))
    else:
        for source,db_level in sounds.items():
            if db_level<input_sound_level:
                return(print(f"sound between {source} : {db_level} and {right_limit[0]} :{right_limit[1]}"))
            else:
                right_limit=[source,db_level]
# ex5()

"""================================================Exercicio 4:========================================================================
Faca um programa que imprima na tela se um dado ano e bissexto ou nao de acordo com as regras na ordem abaixo:
Um ano que e divisivel por 400 e bissexto.
Dos anos que nao entram na regra 1, se o ano for divisivel por 100 entao ele nao e bissexto.
Dos anos que nao entram na regra 2, se o ano for divisivel por 4 entao ele e um ano bissexto.
Todos os outros anos nao sao bissextos
"""
def ex4():
    ano=int(input("digite o ano: "))
    if ano%400:
        print(f"o ano {ano} é bissexto")
    elif ano%100==0:
        print(f"o ano {ano} nao é bissexto")
    elif ano%4==0:
        print(f"o ano {ano} é bissexto")
    else:
        print(f"o ano {ano} nao é bissexto")
# ex4()

"""================================================Exercicio 5:========================================================================
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com tres letras, um traco e quatro numeros. Exemplos: 
Dada a entrada ABT-1234 o programa deveria exibir True
Dada a entrada JKL9999 o programa deveria exibir False
Qualquer outra entrada que fuja do padrao de 3 letras, um traco e quatro numeros, o programa devera exibir False
"""
import string

def ex5():
    plate=input("digite a placa: ")

    for i in plate[:3]:
        if i in string.ascii_uppercase:
            continue
        else:
            return(print(False))
    if plate[3]!="-":
        return(print(False))
    for i in plate[4:]:
        if int(i) not in range(10):
            return(print(False))
    return(print(True))
# ex5()