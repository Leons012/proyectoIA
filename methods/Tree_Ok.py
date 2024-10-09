# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:01:39 2020
Ok.
@author: ferna
"""

#Clase Nodo


class Node:
    #Metodo constructor de la clase, da estado inicial a la clase
    def __init__(self, data, son=None):
        self.data = data
        self.son = None
        self.father = None
        self.cost = None
        self.set_son(son)

#metodo set_son
    def set_son(self, son):
        self.son = son
        if self.son is not None:
            for s in self.son:
                s.father = self
#metodo get_son , retorna una lista con los hijos del nodo
    #self=hace referencia a los objetos que pertenezcan a la clase
    def get_son(self):
        return self.son

#retorna el nodo padre
    def get_father(self):
        return self.father
    
    # asigna el nodo padre de este nodo

    def set_father(self, father):
        self.father = father
        
        #asigna un dato al nodo

    def set_data(self, data):
        self.data = data

#Devuel el dato almacenado en el nodo
    def get_data(self):
        return self.data

#metod que asigna un peso al nodo dentro del arbol
    def set_cost(self, cost):
        self.cost = cost

        #Devuelve el pseo del nodo dentro del arbol
    def get_cost(self):
        return self.cost

#Devuelve verdadero si el dato contenido en el nodo es igual al nodo pasado comomparamtero
    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

#devuelve verdadero si el dato contenido en el nodo es = a algunos de los nodos contenidos en la lista de nodos
            #pasados como parametros.
    def on_list(self, node_list):
        listed = False
        for n in node_list:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_data())