"""Lista de exercicios
Tema: dicionarios e sets
Diversao do carnaval \o/
"""


"""================================================Exercicio 1:========================================================================
Digamos que existam 2 cursos de idiomas em uma escola, ingles e frances, e que existam alunos matriculados conforme abaixo:
Alunos matriculados em ingles:
Joao Alves dos Santos
Maria Magalhaes
Antonio da Silva Ferreira
Jose Junior Jarbas
Henrique da Silva Sauro
Joaquina Ferreira da Silva
Fabiana Aparecida Bianco
Marrone Gutierres
Carlos Magno Farad
Antonio da Silva Junior Amaral

Alunos matriculados em frances:
Joao Alves dos Santos
Antonio da Silva Ferreira
Fernanda Abdala Mohamed
Abner Mignon Alib
Alisson Figueiredo
Henrique da Silva Sauro
Maria Magalhaes
Marrone Gutierres
Joaquina Ferreira da Silva
Faca um programa que responda as seguintes perguntas:
Quantos alunos estao matriculados na escola, no total?
Quantos e quais estao matriculados APENAS em INGLES?
Quantos e quais estao matriculados APENAS em FRANCES?
Quantos e quais estao matriculados EM AMBOS os cursos?
Quantos alunos estao matriculados somente em frances ou somente em ingles, mas nao em ambos os cursos?
"""
from numpy import sort


def ex1():
    set_english={"Joao Alves dos Santos","Maria Magalhaes","Antonio da Silva Ferreira",
    "Jose Junior Jarbas","Henrique da Silva Sauro","Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco","Marrone Gutierres","Carlos Magno Farad","Antonio da Silva Junior Amaral"}

    set_french={"Joao Alves dos Santos","Antonio da Silva Ferreira","Fernanda Abdala Mohamed",
    "Abner Mignon Alib","Alisson Figueiredo","Henrique da Silva Sauro","Maria Magalhaes","Marrone Gutierres","Joaquina Ferreira da Silva"}
    
    print(f"Quantos alunos estao matriculados na escola, no total? {len(set_english.union(set_french))}")
    print(f"Quantos e quais estao matriculados APENAS em INGLES?\n Matriculados apenas em ingles {len(set_english)}\n e sao os alunos {set_english}")
    print(f"Quantos e quais estao matriculados APENAS em FRANCES?\n Matriculados apenas em frences {len(set_french)}\n e sao os alunos {set_french}")
    print(f"Quantos e quais estao matriculados EM AMBOS os cursos?\n Matriculados em ambos {len(set_french&set_english)}\n e sao:{set_french&set_english}")
    print(f"Quantos alunos estao matriculados somente em frances ou somente em ingles, mas nao em ambos os cursos?\n Somente em ingles: {len(set_english-set_french)}\n Somente em frances: {len(set_french-set_english)}\n para um total de: {len(set_english-set_french)+len(set_french-set_english)}")

# ex1()

"""================================================Exercicio 2:========================================================================
Faca um programa que le uma sigla de um estado do usuario e imprime na tela o nome completo do estado. Exemplo:
>>> Digite um estado: SP
>>> O nome completo do estado e Sao Paulo.
"""
def ex2():
    states_={"SP":"Sao Paulo","MG":"Minas Gerais","RJ":"Rio de Janeiro"}
    key_=input("Digite a sigla do estado: ")
    print(f"o nome completo do estado e {states_[key_]}")

# ex2()

"""================================================Exercicio 3:========================================================================
Faca um programa que ordene um dicionario por seus valores. Exemplo: dado o dicionario
>>> {"matematica": 81, "fisica": 83, "quimica": 87} 
a saida deve ser 
>>> {"quimica": 87, "fisica": 83, matematica": 81}
"""
def ex3():
    input_dictionary={"matematica": 81, "fisica": 83, "quimica": 87}
    reordered=dict()
    ordered_values= list(input_dictionary.values())
    ordered_values.sort(reverse=True)    #sort a list of the values in the dictionary

    for i in ordered_values:
        key_list=list(input_dictionary.keys())
        pos_value_in_list=list(input_dictionary.values()).index(i)
        reordered[key_list[pos_value_in_list]]=i

    print(reordered)


# ex3()

"""================================================Exercicio 4:========================================================================
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionario. Exemplo: dada o dicionario
>>> {1: "vermelho", 2: "azul", 3: "marrom"}
A saida devera ser
>>> {1: 8, 2: 4, 3: 6}
"""
def ex4():
    dictionary={1: "vermelho", 2: "azul", 3: "marrom"}
    for key,value in dictionary.items():
        dictionary[key]=len(value)
    print(dictionary)
# ex4()

"""================================================Exercicio 5:========================================================================
Faca um programa que encontre as notas minimas e maximas de um dicionario, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionario
>>> {"Theodoro": 20, "Marcia": 50, "Junior": 80}
A saida deve ser
>>> Nota maxima -> Junior : 80
>>> Nota minima -> Theodoro : 20
"""
def ex5():
    scores={"Theodoro": 20, "Marcia": 50, "Junior": 80}
    min_score=min(list(scores.values()))
    max_score=max(list(scores.values()))

    print(f"Nota maxima -> {list(scores.keys())[list(scores.values()).index(max_score)]} : {max_score}")
    print(f"Nota minima -> {list(scores.keys())[list(scores.values()).index(min_score)]} : {min_score}")
# ex5()

print("\n=================END====================")