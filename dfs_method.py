from Tree_Ok import Node

# Función para construir los nodos a partir del diccionario
def construir_nodos(conexiones):
    nodos = {}
    for ciudad, vecinos in conexiones.items():
        nodos[ciudad] = Node(ciudad)  # Creamos el nodo para la ciudad

    # Ahora configuramos los hijos (son)
    for ciudad, vecinos in conexiones.items():
        nodos[ciudad].set_son([nodos[vecino] for vecino in vecinos])
    
    return nodos

# Función DFS utilizando la clase Node
def dfs_node(inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = []
    if camino is None:
        camino = []

    visitados.append(inicio)
    camino.append(inicio)

    # Si hemos llegado al objetivo, retornamos el camino encontrado
    if inicio.get_data() == objetivo.get_data():
        return camino

    # Recorremos los hijos del nodo actual
    for hijo in inicio.get_son():
        if not hijo.on_list(visitados):
            resultado = dfs_node(hijo, objetivo, visitados, camino)
            if resultado:  # Si encontramos el objetivo en alguna rama
                return resultado

    # Si no encontramos el objetivo, retrocedemos (backtracking)
    camino.pop()
    return None

def searchDFS(b1, b2, conexiones):
    # Construimos los nodos a partir del diccionario
    nodos = construir_nodos(conexiones)
    
    # Establecemos el nodo de inicio y de destino
    inicio = nodos[b1]
    objetivo = nodos[b2]
    
    # Ejecutamos la búsqueda DFS
    camino_encontrado = dfs_node(inicio, objetivo)

    print(tuple(str(n) for n in camino_encontrado))
    
    # Imprimimos el resultado
    if camino_encontrado:
        return tuple(str(n) for n in camino_encontrado)
    else:
        return ("No se encontró un camino.")