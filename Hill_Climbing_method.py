# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:30:58 2020
# VRP_CIUDADES ESPAÑA
@author: ferna
"""
# TSP con hill climbing
import math
import random
 
def distancia(coord1, coord2):
     lat1=coord1[0]
     lon1=coord1[1]
     lat2=coord2[0]
     lon2=coord2[1]
     return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)
 
    # calcula la distancia cubierta por una ruta
def evalua_ruta(ruta, coord):
        total=0
        for i in range(0,len(ruta)-1):
            ciudad1=ruta[i]
            ciudad2=ruta[i+1]
            total=total+distancia(coord[ciudad1], coord[ciudad2])
        ciudad1=ruta[i+1]
        ciudad2=ruta[0]
        total=total+distancia(coord[ciudad1], coord[ciudad2])
        return total
        
def hill_climbing(coord):
    # crear ruta inicial aleatoria
        ruta=[]
        for ciudad in coord:
            ruta.append(ciudad)
        random.shuffle(ruta)
        
        mejora=True
        while mejora:
            mejora=False
            dist_actual=evalua_ruta(ruta, coord)
            # evaluar vecinos
            for i in range(0,len(ruta)):
                if mejora:
                    break 
                for j in range(0,len(ruta)):
                    if i!=j:
                        ruta_tmp=ruta[:]
                        ciudad_tmp=ruta_tmp[i]
                        ruta_tmp[i]=ruta_tmp[j]
                        ruta_tmp[j]=ciudad_tmp
                        dist=evalua_ruta(ruta_tmp, coord)
                        if dist<dist_actual:
                            # encontrar vecino que mejora el Resulatdo
                            mejora=True
                            ruta=ruta_tmp[:]
                            break
        return ruta

def searchHillClimbing(coord):
    ruta = hill_climbing(coord)
    return (ruta, str(evalua_ruta(ruta, coord)))
                            
        


