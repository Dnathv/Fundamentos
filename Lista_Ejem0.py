# Programa: Lista_Ejem0                                  Feb/2026
# Autor: Daniel Barajas y Valencia
# Objetivo: Manejo de listas (arreglos) y de la funcion "append()"         
#   Ejemplo: Suponiendo que "X" es una lista:  X.append(dato)
#           el dato se agrega al final de la lista X. 
# Problema: Definir la lista A y el numero n de elementos.
#   Leer y almacenar los valores enteros y escribir como quedo la lista.

print ('Se genera la lista A (lista vacia)\n')
A = []                                  # lista vacia
n = int (input("Numero de valores: "))

for i in range(1, n+1):
    V = int ( input("Valor: ") )
    A.append(V)                         # el dato V se agrega a la lista

print ('\nLa lista A es = \n')
print (A)

print ('\nProceso terminado..')

"""
Se genera la lista A (lista vacia)

Numero de valores: 5
Valor: 34
Valor: -25
Valor: 12
Valor: 0
Valor: 36

La lista A es = 

[34, -25, 12, 0, 36]
"""
