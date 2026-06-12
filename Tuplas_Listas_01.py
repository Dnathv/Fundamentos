# Programa: Tuplas_Listas_01                         12.JUN.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Definicion y manejo de tuplas.
# Problema: Generar la tupla "Grados" y efectuar diversas operaciones como:
#   Accesar a elemntos de la tupla, medir su tamaño, desempaquetar, pasar 
#   una lista a una tupla.

print ("1.- Generar la tupla Grados:")
Grados = (10, 20, 30)
print (Grados) 

print ("\n2.- Recorrer la tupla")
for i in Grados:
    print (i)

print ("\n3.- Medir el tamaño de la tupla")
print ("El tamaño de la tupla es: ", len (Grados))

print ("\n4.- Desempaquetar la tupla")
(d1, d2, d3) = Grados
print ("Los datos desempaquetados son: ", d1, d2, d3)

print ("\n5.- Pasar una lista a una tupla")
L = [25, -12, 43]
T1 = tuple(L)
print ("La tupla T1 tiene los siguientes datos: ", T1)

print ("\nProceso terminado")
input ("Presione <Enter> para finalizar")