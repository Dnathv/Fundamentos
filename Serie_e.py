# Programa: Serie_e                       12.Marzo.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de una serie numerica con la estructura de
#      repeticion "for" y de la funcion de usuario "FactR".
# Problema: Calcular el numero Euler "e" con la siguiente serie numerica 
#      e = 1/1! + 2/2! + 3/3! + ..... n/n!
#   El numero de terminos "n" se debe introducir por el teclado.

import math

#Definicion de la funcion Fact
def FactR(n):
    if (n <= 0):
        return (1)
    else:
        F = 1
        for i in range(1, n+1):
            F = F * i
        return (F)

print ("Calculo del numero Euler e")
n = int (input("Numero de terminos: "))
suma = 0
print (" ")
print ('



print ("\nProceso terminado")
