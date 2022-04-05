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

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
"""
from numpy import sort


def ex1():
    set_english={"Joao Alves dos Santos","Maria Magalhaes","Antonio da Silva Ferreira",
    "Jose Junior Jarbas","Henrique da Silva Sauro","Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco","Marrone Gutierres","Carlos Magno Farad","Antonio da Silva Junior Amaral"}

    set_french={"Joao Alves dos Santos","Antonio da Silva Ferreira","Fernanda Abdala Mohamed",
    "Abner Mignon Alib","Alisson Figueiredo","Henrique da Silva Sauro","Maria Magalhaes","Marrone Gutierres","Joaquina Ferreira da Silva"}
    
    print(f"Resp 1) - {len(set_english.union(set_french))}")
    print(f"Resp 2) - {len(set_english)-len(set_french)} e sao os alunos {set_english-set_french}")
    print(f"Resp 3) - Matriculados apenas em frences {len(set_french)-len(set_english)} e sao os alunos {set_french- set_english}")
    print(f"Resp 4) - Matriculados em ambos {len(set_french&set_english)}\n e sao:{set_french&set_english}")
    print(f"Resp 5) -  Somente em ingles: {len(set_english-set_french)}\n Somente em frances: {len(set_french-set_english)}\n para um total de: {len(set_english-set_french)+len(set_french-set_english)}")

    # print(f"Resp 5) - {len(alunos_ingles.symmetric_difference(alunos_frances))}")
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

"""=================GABARITO====================================
### Explicação!
# Usei a função `sorted` para ordenar nosso dicionário passando algun argumentos extras
# Link da documentação oficial da função `sorted`: https://docs.python.org/3/library/functions.html#sorted

# dict_to_order.items() -> retorna uma lista de tuplas com chaves e valores de um dicionário: [("matemática", 81), ("física", 83), ("química", 87)]
# O argumento `key` precisa ser uma função (veja na documentação oficial).
# Para esse argumento usei uma função anônima lambda que faz o seguinte: dado uma tupla, retorna o segundo valor dela (índice 1)
# Obs: lembre-se que a indexação começa por zero, então o índice 1 é o segundo valor, que refere-se aos valores do dicionário

# Basicamente o argumento `key` está nos dizendo que devemos ordenar pelos segundos elementos das tuplas de chave-valor!
# Usamos o argumento `reverse=True` para definir a ordem decrescente

# O resultado disso tudo é uma lista de tuplas ordenadas pelo segundo elemento (valor do dicionário)
# [("química", 87), ("física", 83), ("matemática", 81)]
ordered_dict = dict(sorted(dict_to_order.items(), key=lambda tupla: tupla[1], reverse=True))

"""
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