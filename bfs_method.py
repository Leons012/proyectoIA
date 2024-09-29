# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:51:04 2020

@author: ferna
"""
# Vuelos con búsqueda en amplitud 
from arbol import Nodo 
def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[] 
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    #resultado=0
    while (not solucionado) and len(nodos_frontera)!=0:
        nodo=nodos_frontera[0] 
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encontrada 
            solucionado=True
            return nodo
        else:
                # expandir nodos hijo (ciudades con conexión) 
            dato_nodo = nodo.get_datos()
            lista_hijos=[] 
            for un_hijo in conexiones[dato_nodo].keys():
                hijo=Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) \
                and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
                    
            nodo.set_hijos(lista_hijos)

def searchBFS(b1, b2, connections):             
    nodo_solucion = buscar_solucion_BFS(connections, b1, b2)
    
    #Mostrar resulatdo
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(b1)
    resultado.reverse()
    return (' -> '.join(resultado))


        

