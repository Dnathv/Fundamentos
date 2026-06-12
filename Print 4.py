# Programa: Printing_4            19.02.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicar algunas funciones naturales.
# Problema: Calcular e imprimir el resultado del seno,
#    coseno, tangente, del angulo que debe introducirse 
#    por el teclado.
# NOTA: Escribir los 5 resultados con una sola instruccion

import math    
from math import *

ang = int (input("angulo en grados: "))

rad = ang*pi/180
S = math.sin(rad)
C = math.cos(rad)
T = math.tan(rad)

print ("\nValores de: ang, rad, seno, coseno, tang\n")
print (ang,rad,S,C,T)

print ('{0:3d} {1:8.3f} {2:10.6f} {3:10.6f} {4:10.6f}'.
       format(ang, rad, S, C, T))

print("\nProceso terminado")
