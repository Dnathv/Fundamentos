# Programa: Tuplas_modif2                           12.JUN.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso y aplicacion de tuplas.
# Problema: Generar la tupla "TD" con 4 datos.
#   Pregunta cual de los cuatro se quiere modificar y pedir el nuevo valor.
#   Con append() agrgar cada dato de la tupla TD a la lista que debe 
#   empezar vacia. En la lista hacer el cambio pedido y con la funcion tuple() 
#   la lista se convierte en la nueva tupla TD2.

print ("1.- Generar la tupla TD con cuatro datos:")
print ("10, 20, 30, 40")
TD = (10, 20, 30, 40)
print ("La tupla TD tiene 4 datos")

print ("\n2.- Preguntar cual de los cuatro datos se quiere modificar y pedir el nuevo valor")
(d1, d2, d3, d4) = TD             #La TD se desempaca
Num = int(input("Dato a modificar: 1, 2, 3, 4: "))
val = input("Nuevo valor = ")
if Num == 1:
    d1 = int(val)
elif Num == 2:
    d2 = int(val)
elif Num == 3:
    d3 = int(val)
else:
    d4 = int(val)
    
print ("\n3.- Con append() agregar cada dato de la tupla TD a la lista que debe empezar vacia")
L = []          #Lista vacia
L.append (d1)
L.append (d2)
L.append (d3)
L.append (d4)

print ("\n4.- En la lista hacer el cambio pedido y con la funcion tuple() la lista se convierte en la nueva tupla TD2")
TD2 = tuple (L)
print (" Tupla inicial TD: ", TD)
print (" Nueva tupla TD2: ", TD2)   

print ("\n Proceso  terminado")
input ("Presione <Enter> para finalizar")