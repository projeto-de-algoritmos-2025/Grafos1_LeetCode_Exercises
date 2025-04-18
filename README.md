# NomedoProjeto

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2063462 |  Samuel Alves Silva |
| 20/0024949  |  Matheus Ferreira Diogo |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 1 média) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Grafos 1) da disciplina. 

## Screenshots
### [785 - Média](https://leetcode.com/problems/is-graph-bipartite/)
A solução usa DFS para tentar colorir o grafo com duas cores alternadas (0 e 1). Começamos colorindo o nó de forma arbitrária (0), e a cada passo colorimos os vizinhos com a cor oposta. Se algum vizinho já tiver a mesma cor, o grafo não é bipartido e retornamos false. Como o grafo pode ser desconexo, percorremos todos os nós, iniciando a DFS nos que ainda não foram coloridos. A função retorna true se todas as componentes do grafo forem bipartidas.

![785](/assets/785.png)

### [332 - Difícil](https://leetcode.com/problems/reconstruct-itinerary/description/)
Essa solução usa DFS com uma fila de prioridade (min-heap) para garantir que, a partir de cada aeroporto, o próximo destino escolhido seja o menor em ordem alfabética. O grafo é percorrido começando por "JFK", removendo as passagens à medida que são usadas. No final, o itinerário é invertido para refletir a ordem correta, garantindo que todas as passagens sejam usadas e o caminho seja o menor lexicograficamente.

![332](/assets/332.PNG)

## Instalação 
**Linguagem**: Python<br>

## Outros 
...
