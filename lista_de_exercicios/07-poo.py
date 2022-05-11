"""Lista de exercicios

Tema: POO

"""

"""===============Exercicio 1:===============
Escreva uma classe que converta numeros inteiros para numeros romanos.

"""
# ---------------Implement--------------------------
# Def error when placing 4 equal letters in sequence
# ccm IS INCORRECT YOU CAN ONLY SUBTRACT GROUPS OF TWO NUMBERS

class RomanNumber:
    def __init__(self,roman_num:str):
        self.roman_num:str=roman_num

    def convert_arabic(self)->int:
        roman_values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        roman_number=self.roman_num
        arabic_number=0
        added_value=[]
        while i<len(roman_number):
            number=roman_values[roman_number[i]]

            if added_value==[]:
                added_value.append(number)

            elif number==added_value[-1]:
                added_value.append(number)

            elif number>added_value[-1]:
                arabic_number+=number-sum(added_value)
                added_value=[]
                    
            else:
                arabic_number+=sum(added_value)
                added_value=[]
                continue
            i+=1

        arabic_number+=sum(added_value)
        return arabic_number

roman_number=RomanNumber("MCMXCIV")
# roman_number=RomanNumber("DCCCL")

print(roman_number.convert_arabic())

"""===============Exercicio 2:===============
Escreva uma classe que converta numeros romanos para numeros inteiros.

"""
class ArabicNumber:
    ROMAN_VALUES={1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

    def __init__(self,number):
        self.number:int=number

    def convert_roman(self)->str:
        arabic_number = self.number
        roman_number = ""
        while arabic_number>0:
            for position,(arabic_value,roman_value) in enumerate(self.ROMAN_VALUES.items()):
                int_value = arabic_number//arabic_value
                if 3>= int_value >=1:
                    roman_number += roman_value*int_value
                    arabic_number += -int_value*arabic_value

                if arabic_number % arabic_value>=0.8*arabic_value:
                    if lower_num == arabic_value/2:
                        lower_num = list(self.ROMAN_VALUES.keys())[position+2]
                    else:
                        lower_num = list(self.ROMAN_VALUES.keys())[position+1]
                        
                    roman_number += self.ROMAN_VALUES[lower_num]+self.ROMAN_VALUES[arabic_value]
                    arabic_number += -(arabic_value-lower_num)
        
        return(roman_number)


arabic_num=ArabicNumber(1994)
print(arabic_num.convert_roman())

"""===============Exercicio 3:===============
Infelizmente a classe nativa do Python list nao tem alguns calculos muito

utilizados: medias. Construa uma classe chamada ListaPersonalizada que herde

todas as funcionalidades da classe nativa e acrescente os calculos de media

simples e ponderada.

"""

class ListaPersonalizada(list):
    def __init__(self,lista:list):
        self.list_elements:list=lista
    
    def average(self)->float:
        return sum(self.list_elements)/len(self.list_elements)

    def weighted_average(self,weights:list)->float:
        sum_=0
        for i in range(len(weights)):
            sum_+=weights[i]*self.list_elements[i]
        return sum_/sum(weights)

lista1=ListaPersonalizada([2,4,5,1,2])
print(lista1.average())
print(lista1.weighted_average([1,5,7,6,1]))

"""===============Exercicio 4:===============


Implemente uma classe chamada Poligono que servira de base para outras classes

(classe mae). Esta classe deve ter metodos para calcular area e perimetro. A

partir desta classe, crie subclasses para cada poligono especifico: Triangulo,



Quadrado, Pentagono. Cada um deles deve sobrescrever o metodo da classe mae

para implementar a sua propria formula de calculo de area e perimetro.
"""
from abc import ABC,abstractmethod
from math import sqrt

class Polygon(ABC):
    def __init__(self,side_lenght:int):
        self.side:int=side_lenght

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self,side_lenght:int):
        super().__init__(side_lenght)
    
    def area(self):
        return sqrt(3/4)*self.side**2 

    def perimeter(self):
        return self.side*3

class Square(Polygon):
    def __init__(self,side_lenght:int):
        super().__init__(side_lenght)
    
    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4
    
class Pentagon(Polygon):
    def __init__(self,side_lenght:int):
        super().__init__(side_lenght)
    
    def area(self):
        return 1/4*sqrt(5*(5+2*sqrt(5)))*self.side

    def perimeter(self):
        return self.side*5
    


"""===============Exercicio 5 (desafio):===============
Como voce reduziria a quantidade de estruturas if-else no codigo abaixo

usando heranca e polimorfismo?

# ...

class Passaro:

# ...

def calcula_velocidade(self):

if self.tipo == "EUROPEU":

return self.calcula_veloridade_base()

elif self.tipo == "AFRICANO":

return self.calcula_veloridade_base() - self.calcula_fator_carga() * self.altura_maxima_de_voo

elif self.tipo == "NORUEGUES":

return 0 if self.nao_voa else calcula_veloridade_base()

# ...

"""

class Bird:
    def __init__(self,altura_maxima_de_voo):
        self.altura_maxima_de_voo=altura_maxima_de_voo

    def calcula_velocidade(self):
        pass

    def calcula_fator_carga(self):
        pass

class African(Bird):
    def __init__(self,altura_maxima_de_voo):
        super().__init__(altura_maxima_de_voo)


    def calcula_velocidade(self):
        return self.calcula_velocidade_base() - self.calcula_fator_carga() * self.altura_maxima_de_voo
    pass

class European(Bird):
    def __init__(self,altura_maxima_de_voo):
        super().__init__(altura_maxima_de_voo)

    def calcula_velocidade(self):
        return self.calcula_velocidade_base()

class Norwegian(Bird):
    def __init__(self,altura_maxima_de_voo):
        super().__init__(altura_maxima_de_voo)

    def calcula_velocidade(self):
        return self.calcula_velocidade_base()

class nao_voa(Norwegian):
    def __init__(self,altura_maxima_de_voo):
        super().__init__(altura_maxima_de_voo)

    def calcula_velocidade(self):
        return 0