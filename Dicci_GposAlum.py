# Programa: Dicci_GposAlum                                 12.Jun.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de diccionarios
# Problema: Definir el diccionario Asig...
#   Los valores del diccionario son listas.

print ("Definir el diccionario Asig con lo siguiente: ")
print ("Algebra:      3 grupos de 20, 30 y 25 alumnos")
print ("Aritmetica:   2 grupos de 17 y 40 alumnos")
print ("Calculo:      1 grupo de 15 alumnos")

Asig = {"Algebra":[20,30,25], "Aritmetica":[17,40,20], "Calculo":[15,15,15]}
input ()
print ("El diccionario Asig quedo como: ")
print (Asig)

L1 = (Asig["Algebra"])
print ("\nTotal de Alumnos en Algebra: ", sum(L1))
L2 = (Asig["Aritmetica"])
print ("\nTotal de Alumnos en Aritmetica: ", sum(L2))
L3 = (Asig["Calculo"])
print ("\nTotal de Alumnos en Calculo: ", sum(L3))

print ("\nProceso terminado")
