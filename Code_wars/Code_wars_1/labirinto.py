"""===============|Grupo|==================================================
Lígia Pereira Silva de Oliveira---------(https://github.com/Ligia-PSO)								
Letícia Arroyo Torres-------------------(______________________________)								
Henrique Cezar Cândido Xavier Ferreira--(https://github.com/henrique-cxf)								
Lucas Borges Fernandes------------------(https://github.com/LucasBF00)								
Vinicius Miranda Santos-----------------(https://github.com/vinicius261)						
==========================================================================="""
from time import sleep
from generate_map import generate_maze

def input_user_maze(h:int=10,c:int=20)->list:
    """gera um labirinto aleatorio com o tamanho definido pelo usuario"""
    while True:
        user_response=input("Deseja mudar o tamanho do labirinto do padrao 10x20 ?(y/n) ").upper()
        if user_response=="Y":
            h=int(input("Qual a altura do labirinto? "))
            c=int(input("Qual o comprimento do labirinto? "))
            break
        elif user_response=="N":
            break
        else:
            print("Resposta invalida")

    return generate_maze(h,c)

def print_maze(maze_map:list)->None:
    """printa o labirinto com os numeros das colunas e linhas alinhados"""
    l_size=len(str(l-1))#maximas casas decimais do numero de linhas do labirinto
    c_size=len(str(c-1))#maximas casas decimais do numero de colunas do labirinto
    
    #padronizando numeros com mesmas casas decimais
    line_list=map(lambda n:str(n).zfill(l_size),range(l))
    column_numbers=map(lambda n:str(n).zfill(c_size),range(c))

    spacing=" "*c_size #espacamento necessario entre as colunas
   
    print(" "*(l_size+1) + " ".join(column_numbers))
    for i in line_list:
        print(i + spacing + spacing.join(maze_map[int(i)]))   
    return None

def user_input(maze_map:list)->tuple:#pega a posicao inicial do usuario e verifica se e valido ex:"1,2"
    i,j=tuple(map(int,input("Onde deseja colocar o robo?(ex:3,4)").split(",")))
    while True:
        if maze_map[i][j]==" ":#posicao e valida
            break
        print("O robo nao pode ser posto nessa posicao insira uma nova posicao")
        i,j=tuple(map(int,input("Onde deseja colocar o robo?").split(",")))

    maze_map[i][j]="X"
    return maze_map,(i,j)    

def verify_movement(position:tuple,direction:list)->tuple:
    """Verifica se a direcao de movimentacao e possivel"""
    i,j=[x + y for x, y in zip(position, direction)]
    if 0<=i<l and 0<=j<c:
        if maze_map[i][j]!="#":# A direcao nao e uma parede e se encontra nos limites do labirinto 
            return True,i,j
    return False,i,j

def move_robot(position:tuple,)->None:
    """movimenta o robo ate a saída"""
    ESQUERDA = [0, -1]
    DIREITA  = [0, 1]
    CIMA     = [-1, 0]
    BAIXO    = [1, 0]  
    visited_positions=[]
    
    while True:
        sleep(0.7)#espera 0,7 segundos para rodar o proximo movimento do robo
        maze_map[position[0]][position[1]]="."#marca a posicao atual como percorrida
        directions_dict=dict()
        for direction in [CIMA,DIREITA,BAIXO,ESQUERDA]:
            verify_result,i,j=verify_movement(position,direction)
            if verify_result:
                directions_dict[(i,j)]=maze_map[i][j]#adiciona aos caminhos possiveis de serem tomados pelo robo

        if "S" in directions_dict.values():
            i,j=list(directions_dict.keys())[list(directions_dict.values()).index("S")]
            maze_map[i][j]="X"
            print_maze(maze_map)
            print("========|Saída Encontrada|========")
            return None

        elif " " in directions_dict.values():
            chosen_direction=list(directions_dict.keys())[list(directions_dict.values()).index(" ")]
            visited_positions.append(position)
        else:
            chosen_direction=visited_positions.pop(-1)
            if len(visited_positions)==0:#todas as regioes possiveis de percorrer foram visitadas
                print("========|Beco sem saída|========")
                return None

        position=chosen_direction#a direcao escolhida vira a nova posicao do robo
        maze_map[position[0]][position[1]]="X"
       
        print("\n")
        print_maze(maze_map)

if __name__ == "__main__":

    maze_map=input_user_maze()
    l=len(maze_map)#numero de linhas
    c=len(maze_map[0])#numero de colunas
    print_maze(maze_map)
    maze_map,position=user_input(maze_map)#pega a posicao inicial do robo dada pelo usuario
    print_maze(maze_map)
    move_robot(position)