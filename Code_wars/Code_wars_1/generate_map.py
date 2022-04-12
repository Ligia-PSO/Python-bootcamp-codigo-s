from random import choice
def generate_maze(height:int=10,length:int=20)->list:
    """Gera um labirinto aleatorio com as dimensoes desejadas"""

    map_matrix=[]#inicia matriz do labirinto
    fillers=["#"," "," "]#uma entre 3 chances de preencher o local no labirinto com uma parede
    for i in range(height):
        line=[]
        for j in range(length):
            element=choice(fillers)
            line.append(element)
        map_matrix.append(line)

    places=[]
    for i in [0,height-1]:#coordenada das bordas superiores e inferiores
        for j in range(length):
            places.append((i,j))

    for j in [0,length-1]:#coordenada das bordas laterais da direita e esquerda
        for i in range(height):
            places.append((i,j))

    i,j=choice(places)#ecolhe uma coordenada para a saida nas bordas do labirinto
    map_matrix[i][j]="S"#marca a saida no mapa

    return(map_matrix)