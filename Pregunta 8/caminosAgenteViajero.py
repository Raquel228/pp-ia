import itertools

# Matriz de adyacencia del grafo
adj_matrix = [
    [0, 3, 5, 2, 11, 7, 8, 10],
    [3, 0, 5, 8, 4, 2, 9, 6],
    [5, 5, 0, 10, 1, 7, 14, 4],
    [2, 8, 10, 0, 12, 5, 2, 14],
    [11, 4, 1, 12, 0, 13, 15, 6],
    [7, 2, 7, 5, 13, 0, 1, 9],
    [8, 9, 14, 2, 15, 1, 0, 3],
    [10, 6, 4, 14, 6, 9, 3, 0]
]

# Función para calcular el peso de un camino
def calcular_peso(camino):
    peso = 0
    for i in range(len(camino) - 1):
        peso += adj_matrix[camino[i]][camino[i + 1]]
    return peso

# Generar todos los posibles caminos del grafo del AGENTE-VIAJERO con 8 nodos y sus pesos
nodos = range(len(adj_matrix))
caminos_pesos = []

# Generar permutaciones de todos los nodos
for permutacion in itertools.permutations(nodos):
    peso = calcular_peso(permutacion)
    caminos_pesos.append((permutacion, peso))

# Imprimir los caminos y sus pesos
for camino, peso in caminos_pesos:
    print(f"Camino: {camino}, Peso: {peso}")
