# Programa: Dicci_01
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de diccionarios.
# Problema: Definir el diccionario "dict" y efectuar diferentes procesos.

dict = { "a" : 1,  "b" : 2, "c" : 3}
print (dict)
print ("Valor de b= ", dict ["b"])

print ("\n Se agrega: m")
dict ["m"] = 99

print ("\n Clasificar por clave")
dict.update ({"Ene" : 31, "Feb" : 29})

D1 = (sorted (dict))
D2 = (sorted (dict, reverse = True))

print (D1)
print (D2)
print (dict)

print ("\nProceso terminado")