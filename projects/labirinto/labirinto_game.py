
from collections import defaultdict
import os
from itertools import chain
from random import choice

#use mypath variable so terminal can be run on any terminal location
def print_map(map_matrix:list)->None:
    print("  "+" ".join([str(i) for i in range(0,12)]))
    row_with_spaces=[' '.join(row) for row in map_matrix]
    for i in range(0,10):
        print(f"{i} {row_with_spaces[i]}")

    return None

def continue_game(maze_map:list)->bool:# check if the exit mas reached
    elements_set=set(list(chain.from_iterable(maze_map)))#se of element symbols in the maze
    if "S" not in elements_set:
        return False
    return True

def input_prompt()->list:
    return list(map(int,input("Onde o robo sera inserido ?").split(",")))

def read_player_input(maze_map:list)->bool:
    valid_input=[]
    player_input=input_prompt()
    while len(valid_input)!=2:
        if maze_map[player_input[0]][player_input[1]]=="#":
            print("O robo nao pode ser posicionado em uma parede escolha outro lugar")
            player_input=input_prompt()
       
        elif maze_map[player_input[0]][player_input[1]]=="S":
            print("O robo nao pode ser posicionado na saida escolha outro lugar")
            player_input=input_prompt()
           
        valid_input.extend(player_input)
    maze_map[valid_input[0]][valid_input[1]]="X"
    return maze_map


def move_robot(maze_map:list)->list:
    for line,column in enumerate(maze_map):
        if "X" in maze_map[line]: 
            i,j=line,column.index("X")#robot coordinates i is line j is column
            maze_map[i][j]="."

    directions=defaultdict(list)
    print(i,j)
    if i!=9:#down possible
        directions[(i+1,j)]=maze_map[i+1][j]
    if i!=0:#up possible
        directions[(i-1,j)]=maze_map[i-1][j]
    if j!=11:#right possible
        directions[(i,j+1)]=maze_map[i][j+1]
    if j!=0:#left possible
        directions[(i,j-1)]=maze_map[i][j-1]

    for position,value in directions.items():
        if value=="S":
            chosen_direction=position
            maze_map[chosen_direction[0]][chosen_direction[1]]="X"
            return maze_map
    

    direction_options=list(filter(lambda position:directions[position]==" ",list(directions.keys())))
   
    if len(direction_options)==0:#need to go back on path taken
        direction_options=list(filter(lambda position:directions[position]==".",list(directions.keys())))    
    chosen_direction=choice(direction_options)

    maze_map[chosen_direction[0]][chosen_direction[1]]="X"

    return maze_map

def read_map(txt_file)->list:
    map_matrix=[]
    map_file=open(mypath+"\\"+txt_file,"r")
    for line in map_file:
        line=line.replace("  "," ").replace("\n","")
        line=line.split(" ")#remove \n elements of line and spaces at the beggining of the map
        for i,element in enumerate(line):
            if element=="":
                line[i]=" "
        map_matrix.append(line)
    return map_matrix

mypath= os.path.dirname(os.path.realpath(__file__))
maze_map=read_map("mapa_labirinto.txt")
# print(maze_map)
print_map(maze_map)
maze_setup=read_player_input(maze_map)
print_map(maze_setup)
while  continue_game(maze_setup):
    maze_setup=move_robot(maze_setup)
    print_map(maze_setup)

print("=====|END|=====")
