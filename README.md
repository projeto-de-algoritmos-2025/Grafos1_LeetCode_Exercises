# NomedoProjeto

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2063462 |  Samuel Alves Silva |
| 20/0024949  |  Matheus Ferreira Diogo |

## Sobre 
Resolução de questões do LeetCode (1 difícil e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Grafos 1) da disciplina. 

## Screenshots
###[785 - Média][]
A solução usa DFS para tentar colorir o grafo com duas cores alternadas (0 e 1). Começamos colorindo o nó de forma arbitrária (0), e a cada passo colorimos os vizinhos com a cor oposta. Se algum vizinho já tiver a mesma cor, o grafo não é bipartido e retornamos false. Como o grafo pode ser desconexo, percorremos todos os nós, iniciando a DFS nos que ainda não foram coloridos. A função retorna true se todas as componentes do grafo forem bipartidas.

## Instalação 
**Linguagem**: Python<br>

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.
