# Programa: Dicci_keyvalue                        12.Jun.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de diccionarios
# Problema: Generar el diccionario "Listado" el cual debe empezar vacio. 
#   Indicar "n" cuantos pares de datos tendra el diccionario.
#   Pedir los "n" datos (clave de tipo entero) y el valor cadena.
#   Con estos datos se genera y se actualiza el diccionario.
#   Se aplica la funcion "update()"
#      Se requiere una clave numerica y un valor (cadena)
#           Listado.update({key:value})

print ("Se declara el diccionario Listado vacio")
Listado = {}       # diccionario vacio
n = int(input("Numero de pares de valores del diccionario: "))
for i in range (0, n):
    key = int(input("Introduzca la clave numerica (key): "))
    value = (input("Intoduzca el valor para la clave correspondiente: "))
    Listado.update({key:value})

print (Listado)

print("\nProceso terminado")
