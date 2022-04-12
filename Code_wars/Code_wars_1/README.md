# Code Wars #1

## Projeto em equipe do Bootcamp Código[s] - Stone 

#### Equipe 43:				
* Henrique Cezar Cândido Xavier Ferreira					
* Letícia Arroyo Torres
* Lígia Pereira Silva de Oliveira
* Lucas Borges Fernandes								
* Vinicius Miranda Santos								
___

### Definições do Projeto

Implementar um sistema em Python que efetue o comportamento de um robô tentando encontrar
a saída de um labirinto.
As inspirações para esse projeto foram: aspiradores de pó automáticos (como o Roomba),
navegação no Google Maps e o problema clássico do Labirinto do Minotauro.
O objetivo do projeto é posicionar um robô em um labirinto e desenvolver a lógica para que ele
percorra esse labirinto em busca da saída, avançando pelas células em branco, respeitando as
paredes e retornando por um caminho caso esteja encurralado. O robô não pode avançar 2 vezes
por um mesmo caminho, assim, ao descobrir que está encurralado pode retornar pelas células
percorridas, mas não avança novamente por este caminho.

### O labirinto

O labirinto é representado por uma matriz de caracteres representando, por
exemplo:
* “ ”: espaço em branco por onde o robô pode caminhar
* “#”: parede, o robô não pode avançar para essa posição
* “.”: posição já percorrida pelo robô
* “S”: saída do labirinto
* “X”: posição atual do robô
  
<a>

### Funcionamento do Script

O usuario pode escolher as dimensoes do labirinto aleatorio gerado ou manter as dimensoes padrao de 10x20.

```
Deseja mudar o tamanho do labirinto do padrao 10x20 ?(y/n) y
Qual a altura do labirinto? 5
Qual o comprimento do labirinto? 10
 ```

Após apresentar o labirinto o usuario deve escolher a posição em que o robô será inserido, devendo essa posição representar um espaço em branco, obrigatoriamente.
```
  0 1 2 3 4 5 6 7 8 9
0   #       # # #   #
1   #
2 # #     # #   # # S
3
4 #   # #         # #
Onde deseja colocar o robo?(ex:3,4)3,1
```
 Uma vez posicionado, o robô inicia seu passeio no labirinto a fim de encontrar a saída. 

Para que o usuário consiga acompanhar o passeio do robô, o labirinto é apresentado na tela a cada passo dado.
```
 0 1 2 3 4 5 6 7 8 9
0   # . . . # # #   #
1   # .   . X
2 # # .   # #   # # S
3   . .
4 #   # #         # #
```
 O robô pode avançar por um caminho nunca percorrido e pode retornar por um caminho já percorrido. Não pode, em nenhuma situação, avançar por um caminho já percorrido.
Para garantir esse comportamento, a cada passo válido dado pelo robô, faz-se a troca do espaço vazio
por um ponto no labirinto, indicando que esta posição já foi visitada, como se ele deixasse uma
marca nas posições em que já passou.

### O robô
O robô  é representado pelo caracter “X” dentro do labirinto e pode caminhar apenas na horizontal e na vertical.
Uma vez posicionado, o robô executa sua regra de movimentação:
* testa a sequência das quatro direções possíveis (acima, à direita, abaixo ou à esquerda)
tentando encontrar a saída (S na matriz). Se encontrá-la, avançar na direção correta e
encerrar o jogo;
* se não encontrar a saída, testara sequência das quatro direções para avançar para uma
casa em branco (espaço vazio na matriz). Na primeira direção em que for possível avançar,
empilhar a sua posição atual, marcar a posição atual como percorrida (ponto na matriz) e
avança;
* caso não consiga avançar para uma posição em branco após testar as 4 direções,retorna para sua posição imediatamente anterior. Para isso, desempilha a última posição empilhada e retornar para ela.
  
O robô repete a regra acima até que encontre a saída.
```
  0 1 2 3 4 5 6 7 8 9
0   # . . . # # # . #
1   # .   . . . . . .
2 # # .   # #   # # X
3   . .
4 #   # #         # #
========|Saida Encontrada|========
```
Se tiver percorrido todos os caminhos possiveis sem encontrar a saída retorna a informação de que se encontra em um beco sem saída sendo impossivel sair do labirinto
```
  0 1 2 3 4 5 6 7 8 9
0   #       #     # .
1 # #   #         # X
2 # # #         # . .
3       #       # # #
4 S         #
========|Beco sem saida|========
```
</a>


