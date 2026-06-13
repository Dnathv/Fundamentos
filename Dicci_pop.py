# Programa: Dicci_pop                                 12.Jun.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de diccionarios
# Problema: Eliminar (pop) un elemento del diccionario "Alumno".

print ("Se tiene el siguiente diccionario Alumno: ")
Alumno = {'Nombre':'Saul', 'Edad':25, 'Ciudad':'Durango',
          'sexo':'Hombre', 'Pais':'Mexico'}
print (Alumno)
input()

print ("Eliminar (pop) del diccionario una clave")
clave = input("Nombre de la clave = ")
print ("Se aplica: Alumno.pop(clave)")

if clave in Alumno.keys():
    valor = Alumno.pop(clave)
    print ("\nEl valor de la clave borrada es: ", valor)
    print ("Ahora se tiene: \n", Alumno)
else:
    print ("\n ¡¡¡La clave NO existe!!! ")

input()

print ("\nProceso terminado")
