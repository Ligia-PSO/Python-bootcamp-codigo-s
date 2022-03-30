"""Lista de exercicios

Tema: listas

Diversao do carnaval \o/

"""
"""================================================Exercicio 1:========================================================================
Crie uma variavel do tipo lista com 5 elementos (voce escolhe quais serao). Imprima na tela o elemento e sua respectiva posicao na lista. Exemplo: para a lista [1, 3, 6, "H", [7,7,7]] a saida deve ser:

>>> Elemento 1 na posicao 0

>>> Elemento 3 na posicao 1

>>> Elemento 6 na posicao 2

>>> Elemento "H" na posicao 3

"""
def ex1():
    elements_list=list()
    n_elements=int(input("how many elements do you wanna add to the list?"))
    for _ in range(n_elements):
        elements_list.append(input("tell the element to be added: "))

    for position,element in enumerate(elements_list):
        print(f"elemento {element} na posicao {position}")
"""================================================Exercicio 2:========================================================================

Crie uma lista com 10 elementos (voce escolhe quais serao) e imprima a lista na ordem inversa. Exemplo: para a lista [1, 3, 6, "H", [7,7,7] a saida deve ser

>>> [[7,7,7], "H", 6, 3, 1]
"""
from calendar import calendar, month

def ex2():
    # list_1=input("inform the 10 elements of the list separated by comma :").split(",")
    list_1=list()
    for i in range(1,11):
        list_1.append(input(f"give list element {i} of 10 :"))

    else:
        list_1.reverse()
        for element in list_1:
            print(element)

"""================================================Exercicio 3:========================================================================

Crie uma lista com 6 numeros inteiros. Imprima o maior, o menor e suas respectivas posicoes. Exemplo: para a lista [5,4,6,8,3,4] a saida deve ser

>>> O maior elemento e 8 e esta na posicao 3

>>> O menor elemento e 3 e esta na posicao 4

Obs: caso o maior ou o menor numero sejam repetidos, trazer a menor posicao.


"""
def ex3():
    list=[5,4,6,8,3,4]
    print(f"O maior elemento e {max(list)} e esta na posicao {list.index(max(list))}")
    print(f"O menor elemento e {min(list)} e esta na posicao {list.index(min(list))}")

"""================================================Exercicio 4:========================================================================

Faca um programa que receba a temperatura media de cada mes do ano e armazene-as em uma lista. Em seguida, calcule a media anual das temperaturas e mostre a media calculada 
juntamente com todas as temperaturas acima da media anual, e em que mes elas ocorreram (mostrar o mes por extenso: Exemplo de saida:

>>> Meses com temperatura acima da media anual de 35,5deg:

>>> 1 - janeiro

>>> 3 - marco

>>> 6 - junho

"""
def ex4():
    import calendar

    temp_year_data=dict()
    months=list(calendar.month_name)[1:]
    for i in range(len(months)):
        specific_month=months[i]
        temp_year_data[specific_month]=float(input(f"Give the mean temperture for the month of {specific_month}:"))

    mean_yearly=sum(temp_year_data.values())/12

    print(f"Years with the temperture above the mean yarly {mean_yearly:10.2f}:")#precision of two decimal places
    for month_1,mean_temp in temp_year_data.items():
        if mean_temp>mean_yearly:
            print(f"{list(temp_year_data.keys()).index(month_1)+1} - {month_1}")

"""================================================Exercicio 5:========================================================================

Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo apos o elemento 6000 na lista acima. O resultado final devera ser:

>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

"""
def ex5():
    lst=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    p1=lst.index([300, 400, [5000, 6000], 500])#posicao da lista onde ele se localiza
    p2=lst[p1].index([5000,6000])#posicao em q se encontra na sublista
    print(lst[p1][p2].append(7000))

    print(lst)
"""================================================Exercicio 6:========================================================================

Faca um programa que remova strings vazias de uma lista de strings. Exemplo: dada a lista ["Ola", "", "meu", "nome", "", "e", "facilitador", ""] a saida deve ser

>>> ["Ola", "meu", "nome", "e", "facilitador"]

"""
def ex6():
        
    list=["Ola", "", "meu", "nome", "", "e", "facilitador", ""]
    for i,value in enumerate(list): #enumerate retorna uma lista de tuplas relacionando a posicao com o elemento ex:[(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3)]
        if value=="":
            list.pop(i)
    print(list)

"""================================================Exercicio 7:========================================================================

Dada a lista de strings ["1", "7", "99", "15"] construa um programa que converte todos os elementos desta lista para inteiro.



Faca tambem o inverso, dada a mesma lista so que agora de elementos inteiros, converta todos os elementos para int.
"""
def ex7():

    lst=["1", "7", "99", "15"]
    for i in range(len(lst)):
        lst[i]=str(lst[i])
    print(lst)
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    print(lst)

print("\n=================END====================")