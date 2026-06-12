# Programa: InvierteArr2                           17.Abr.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Definicion y manipulacion de listas y aplicacion,
#      funciones de usuario "Lee()", "Imp()"
# Problema: Indicar de cuantos elementos "n" sera la lista
#   Con los datos de "A" se calcula la lista "R" cuyos valores
#   seran los de "A" pero en forma invertida.
#   El primero de "A" sera el ultimo de "R"; el segundo sera el
#   penultimo de "R", etc.

def Lee (n):
    L = []
    for i in range (0, n):
        valor = int(input("Valor # " + str(i+1) + ":"))
        L.append (valor)
    return L

def Imp (X):            #imprime los valores de la lista
    for i in X:
        print ('{0:5}',format (i), end = " ")

A = []
R = []
n = int(input("Cuantos valores (Non o impar): "))
A = Lee (n)

k = n-1
for i in range (0, n):
    R.append (A[k])
    k = k-1             #k-=1
Imp (A)
Imp (R)

print ("Proceso terminado")
