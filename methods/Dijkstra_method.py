# -*- coding: utf-8 -*-

import heapq

def dijkstra(grafo, nodo_inicial):
    etiquetas = {nodo_inicial: [0, None]}  # distancia, nodo anterior
    visitados = set()
    cola = [(0, nodo_inicial)]  # (distancia, nodo)
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        
        if nodo_actual in visitados:
            continue
        
        visitados.add(nodo_actual)
        
        for adyacente, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            
            if adyacente not in etiquetas or nueva_distancia < etiquetas[adyacente][0]:
                etiquetas[adyacente] = [nueva_distancia, nodo_actual]
                heapq.heappush(cola, (nueva_distancia, adyacente))
    
    return etiquetas

def construir_camino(etiquetas, nodo_final):
    camino = []
    while nodo_final is not None:
        camino.append(nodo_final)
        nodo_final = etiquetas[nodo_final][1] if nodo_final in etiquetas else None
    camino.reverse()
    return camino

def searchDijkstra(nodo_inicial, nodo_final, grafo):
    etiquetas = dijkstra(grafo, nodo_inicial)
    if nodo_final in etiquetas:
        distancia, _ = etiquetas[nodo_final]
        camino = construir_camino(etiquetas, nodo_final)
        return (camino, distancia)
    else:
        return (f"No se puede llegar al nodo: {nodo_final}")

