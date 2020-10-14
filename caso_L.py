# -*- coding: utf-8 -*-
from reticulado import Reticulado
from barra import Barra
from math import *

def caso_L():
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 

    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N

    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa

    #Parametros
    L = 5.0  *m
    F1 = 9.8*KN
    F2 = 19.6*KN
    B = 2.0 *m
    H = 3.5*m

    #Inicializar modelo
    ret = Reticulado()

    #Nodos
    ret.agregar_nodo(0     , 0   ,  0         ) #0
    ret.agregar_nodo(L     , 0   ,  0         ) #1
    ret.agregar_nodo(2*L   , 0   ,  0         ) #2
    ret.agregar_nodo(3*L   , 0   ,  0         ) #3
    ret.agregar_nodo(L/2   , B/2 , H) #4
    ret.agregar_nodo(3*L/2 , B/2 , H) #5
    ret.agregar_nodo(5*L/2 , B/2 , H) #6
    ret.agregar_nodo(0     , B   , 0          ) #7
    ret.agregar_nodo(L     , B   , 0          ) #8
    ret.agregar_nodo(2*L   , B   , 0          ) #9
    ret.agregar_nodo(3*L   , B   , 0          ) #10
    
    #Barras
    
    r = 8*cm
    A = 3.141592*(r)**2
    t = 5*mm
    props = [r, t, 200*GPa, 0*kg/m**3, 420*MPa]
    
    
    ret.agregar_barra(Barra(0, 1, *props))   # 0
    ret.agregar_barra(Barra(0, 4, *props))
    ret.agregar_barra(Barra(0, 7, *props))
    ret.agregar_barra(Barra(0, 8, *props))
    
    ret.agregar_barra(Barra(1, 2, *props))
    ret.agregar_barra(Barra(1, 4, *props))
    ret.agregar_barra(Barra(1, 5, *props))
    ret.agregar_barra(Barra(1, 7, *props))
    ret.agregar_barra(Barra(1, 8, *props))
    ret.agregar_barra(Barra(1, 9, *props))
    
    ret.agregar_barra(Barra(2, 3, *props))
    ret.agregar_barra(Barra(2, 5, *props))
    ret.agregar_barra(Barra(2, 6, *props))
    ret.agregar_barra(Barra(2, 8, *props))
    ret.agregar_barra(Barra(2, 9, *props))
    ret.agregar_barra(Barra(2, 10, *props))
    
    ret.agregar_barra(Barra(3, 6, *props))
    ret.agregar_barra(Barra(3, 9, *props))
    ret.agregar_barra(Barra(3, 10, *props))
    
    ret.agregar_barra(Barra(4, 5, *props))
    ret.agregar_barra(Barra(4, 7, *props))
    ret.agregar_barra(Barra(4, 8, *props))
    
    ret.agregar_barra(Barra(5, 6, *props))
    ret.agregar_barra(Barra(5, 8, *props))
    ret.agregar_barra(Barra(5, 9, *props))
    
    ret.agregar_barra(Barra(6, 9, *props))
    ret.agregar_barra(Barra(6, 10, *props))

    ret.agregar_barra(Barra(7, 8, *props))
    
    ret.agregar_barra(Barra(8, 9, *props))
    
    ret.agregar_barra(Barra(9, 10, *props))
    
    
    

    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    ret.agregar_restriccion(7, 0, 0)
    ret.agregar_restriccion(7, 1, 0)
    ret.agregar_restriccion(7, 2, 0)
    
    ret.agregar_restriccion(3, 1, 0)
    ret.agregar_restriccion(10, 1, 0)
    
    ret.agregar_restriccion(3, 2, 0)
    ret.agregar_restriccion(10, 2, 0)
    
    ret.agregar_fuerza(0, 2, -F1)
    ret.agregar_fuerza(3, 2, -F1)
    ret.agregar_fuerza(7, 2, -F1)
    ret.agregar_fuerza(10, 2, -F1)
    ret.agregar_fuerza(1, 2, -F2)
    ret.agregar_fuerza(2, 2, -F2)
    ret.agregar_fuerza(8, 2, -F2)
    ret.agregar_fuerza(9, 2, -F2)
    
    return ret