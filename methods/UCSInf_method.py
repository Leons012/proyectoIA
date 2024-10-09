# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:00:25 2024

@author: Fernando Gutierrez
"""
'''*****Se incluye la clase Node******
'''
from math import sin, cos, acos

class Node:
    def __init__(self, datos, padre=None, coste=0):
        self.datos = datos
        self.padre = padre
        self.coste = coste
        self.hijos = []

    def set_coste(self, coste):
        self.coste = coste

    def get_coste(self):
        return self.coste

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_hijos(self, hijos):
        self.hijos = hijos

    def get_hijos(self):
        return self.hijos

    def get_datos(self):
        return self.datos

    def igual(self, nodo):
        return self.datos == nodo.get_datos()

    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

def compara(x, y, coord, solucion):
    # g(n)+h(n) para ciudad x
    lat1 = coord[x.get_datos()][0]
    lon1 = coord[x.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]
    d = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_coste() + d

    # g(n)+h(n) para ciudad y
    lat1 = coord[y.get_datos()][0]
    lon1 = coord[y.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]
    d = int(geodist(lat1, lon1, lat2, lon2))
    c2 = y.get_coste() + d

    return c1 - c2

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    longitud = lon1 - lon2
    val = round((sin(lat1 * grad_rad) * sin(lat2 * grad_rad)) + (cos(lat1 * grad_rad) * cos(lat2 * grad_rad) * cos(longitud * grad_rad)), 12)
    return acos(val) * 111.32

def buscar_solucion_UCS(conexiones, estado_inicial, solucion, coord):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Node(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=lambda x: compara(x, x, coord, solucion))  # se usa lambda ya que sorted no usa cmp en Python 3
        nodo = nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Node(un_hijo)
                # cálculo g(n): coste acumulado
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                hijo.set_padre(nodo)
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

def searchUCSInf(estado_inicial, solucion, conexiones, coord):
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion, coord)
    
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    return (resultado, nodo_solucion.get_coste())




