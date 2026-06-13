# Programa: Dicci_exist                        12.Jun.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de diccionarios
# Problema: Saber si una clave (key) existe en el 
#    diccionario "Paises" y efectuar un calculo.
#      Se pide introducir la clave (key) a buscar
#      Se aplica el operador "if" con "in"

print ("Se tiene el siguiente Diccionario: Paises\n")
print ("Paises = ('Mexico':1 ,'Spain':2 ,'Irak':3 ,'Bosnia':4)")
print ("Cada pais tiene el lugar que ocupo")
Paises = {"Mexico":1 ,"Spain":2 ,"Irak":3 ,"Bosnia":4}
print ("C/pais tiene un premio de 12.5 millon dividido entre el lugar que ocupa")

clave = input("\nIntroducir la clave (key) a buscar: ")

if clave in Paises.keys():
    print ("La clave si existe y su valor (lugar) es: ", Paises[clave])
    R = Paises[clave]
    premio = 12500000/R
    print ("El premio es de $: {0:8.2f}".format(premio))

else:
    print("\n¡La clave no existe!")

print ("\nProceso terminado")
