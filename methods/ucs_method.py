# Busqueda con Coste Uniforme - Uniform Cost Search
from methods.Tree_Ok import Node

def Compare(node):
   return node.get_cost()
#def compare(x,y):
    #return x.get_cost() - y.get_cost()


def search_solution_UCS(connections, init_state, solution):
    solved = False #solucionado
    visited_nodes = [] #nodos visitados
    frontier_nodes = [] #nodos frontera
    init_node = Node(init_state) #nodo inicial
    init_node.set_cost(0)
    frontier_nodes.append(init_node)
    while (not solved) and len(frontier_nodes) != 0:
        # Ordenar lista de nodos frontera. Funcion sorted(ordena nodos frontear)
        frontier_nodes = sorted(frontier_nodes, key=Compare)
        node = frontier_nodes[0]
        # Extraer nodo y añadirlo a visitados
        visited_nodes.append(frontier_nodes.pop(0))
        if node.get_data() == solution:
            # Solucion encontrada
            solved = True
            return node
        else:
            # Expandir nodos hijo (ciudades con conexion)
            node_data = node.get_data()
            child_list = []
            for achild in connections[node_data]:
                child = Node(achild)
                cost = connections[node_data][achild]
                child.set_cost(node.get_cost() + cost)
                child_list.append(child)
                if not child.on_list(visited_nodes):
                    # Si esta en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if child.on_list(frontier_nodes):
                        for n in frontier_nodes:
                            if n.equal(child) and n.get_cost() > child.get_cost():
                                frontier_nodes.remove(n)
                                frontier_nodes.append(child)
                    else:
                        frontier_nodes.append(child)
                    node.set_son(child_list)

def searchUCS(init_state, solution, connections):
    solution_node = search_solution_UCS(connections, init_state, solution)
    # Mostrar resultado
    result = []
    node = solution_node
    while node.get_father() is not None:
        result.append(node.get_data())
        node = node.get_father()
    result.append(init_state)
    result.reverse()
    return (result, str(solution_node.get_cost()))

