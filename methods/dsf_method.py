# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:51:52 2024

@author: salas.iba
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:49:27 2020

@author: ferna

"""

# Busqueda en Profundidad - Depth First Search vuelos
from methods.Tree_Ok import Node

def search_DSF_prof_iter(start_node, solution, connections):
    for limit in range(0, 100):
        visited_nodes = set()
        sol = search_DSF_solution(start_node, solution, visited_nodes, limit, connections)
        if sol is not None:
            return sol
    return None

def search_DSF_solution(node, solution, visited_nodes, limit, connections):
    if limit < 0:
        return None
    
    visited_nodes.add(node.get_data())
    
    if node.get_data() == solution:
        return node
    
    # Expandir nodos hijos - ciudades con conexión
    node_data = node.get_data()
    child_list = []
    for chld in connections.get(node_data, []):
        child = Node(chld)
        if child.get_data() not in visited_nodes:
            child.set_father(node)  # Establecer el padre del nodo hijo
            child_list.append(child)
    
    node.set_son(child_list)
    
    for node_son in node.get_son():
        if node_son.get_data() not in visited_nodes:
            sol = search_DSF_solution(node_son, solution, visited_nodes, limit - 1, connections)
            if sol is not None:
                return sol
    return None

def searchDSF(b1, solution, connections):
    
    init_state = Node(b1)
    solution_node = search_DSF_prof_iter(init_state, solution, connections)
    
    # Mostrar resultado
    if solution_node is not None:
        result = []
        node = solution_node
        while node.get_father() is not None:
            result.append(node.get_data())
            node = node.get_father()
        result.append(init_state.get_data())
        result.reverse()
        return (result)
    else:
        return ("Solución no encontrada")