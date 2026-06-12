# Programa: randint_A3                     20.03.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso del modulo random.randint que genera numeros aleatorios
#   ademas aplicar "for in range ()"
# Problema: Generar e imprimir "n" numeros aleatorios en el rango
#   (inicial y final) indicando. Los valores son: inclusivo.
#   Los valores corresponden al año de nacimiento de algunas personas.
# Se requiere importar la libreria random.

import random

print ("Se generan n numeros aleatorios en un rango de 1993 a 2008")
n = int(input("Cuantos numeros: "))

for x in range (n):              
    R = random.randint(1993, 2008)
    print (R)

print ("\n\nProceso Terminado")
