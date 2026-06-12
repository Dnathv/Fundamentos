# Programa: randint_A2                     20.03.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso del modulo random.randint que genera numeros aleatorios
#   ademas aplicar "for in range ()"
# Problema: Ganerar e imprimir "n" numeros aleatorios en el rango
#   (inicial y final) indicando. Los valores son: inclusivo.
#   Los valores representan estaturas de personas.
# Se requiere importar la libreria random.

import random

print ("Se generan n numeros aleatorios en un rango de 1.50m a 2.10m")
n = int(input("Cuantos numeros: "))

for x in range (n):              
    R = random.randint(1500, 2100)/1000  
    print("{0:10.3f}". format (R, end = ' '))

print ("\n\nProceso Terminado")

