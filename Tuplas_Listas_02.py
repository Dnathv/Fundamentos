# Programa: Tuplas_Listas_02                               12.JUN.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Formacion, aplicacion y modificacion de tuplas.
# Problema: Formar una tupla T1 y modificar el segundo elemento con 
#     el valor de 100.
#     Despues aumentar a la lista el valor "-50"
#     La lista modificada seran los nuevos valores de la tupla:
#       1.- La tupla T1 se convierte en una lista.
#       2.- La lista se puede modificar (cambiar, agregar)
#       3.- Con tuple() la lista se convierte en tupla.

print ("1.- Formar la tupla T1 con los siguientes datos:")
print ("25, -12, 43")
T1 = (25, -12, 43)

print ("\n2.- Modificar el segundo elemento con el valor de 100")
L = list (T1)     #La tupla se convierte en lista
L[1] = 100        #El segundo elemento se modifica
print ("La lista modificada es: ", L) 

print ("\n3.- Aumentar a la lista el valor -50")
L.append (-50)    #Se agrega el valor -50 a la lista
print ("La lista modificada es: ", L)

print ("\n4.- La lista modificada se convierte en tupla")
T1 = tuple (L)    #La lista se convierte en tupla
print ("La tupla modificada es: ", T1)

print ("\nProceso terminado")
input ("Presione <Enter> para finalizar")
