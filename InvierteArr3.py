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
        print ('{0:5}'.format (i), end = " ")

def ImpF (X):
    for i in X:
        print ('{0:7.2f}'.format (i), end = " ")

A = []
R = []
S = []
n = int(input("Cuantos valores (Impar < 2): "))
A = Lee (n)

k = n-1
for i in range (0, n):
    R.append (A[k])
    k = k-1             #k-=1

for i in range (0, n):
    S.append (A[i]/R[i])

print ("\nLos valores de la lista original A son: ")
Imp (A)
print ("\nLos valores de la lista modificada R son: ")
Imp (R)
print ("\nLos valores de la lista modificada S (A/R) son: ")
ImpF (S)

print ("\nProceso terminado")
