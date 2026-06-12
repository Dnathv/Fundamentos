# Programa: Listas Media
# Autor: Gazca Loria Dana Madai
# Objetivo: Definicion y manipulacion de listas y aplicacion de funciones
#      de USUARIO: Lee, Imp, Prom, Prom1, Prom2.
#      de PYTHON: Sum, Ien()
# Problema: Leer los n valores de la lista A y calcular e imprimir la media 
#      o valor promedio de los valores de A. 
# NOTA. El valor de n debe ser mayor de 2 y menor o igual a 30.

def Lee (n):
    L = []
    for i in range (0, n):
        valor = int(input("Valor # " + str(i+1) + ":"))
        L.append (valor)
    return L

def Imp (X):            #imprime los valores de la lista
    for i in X:
        print ('{0:5}'.format (i), end = " ")

def Prom (x):
    S = 0
    for i in range (0,n):
        S = S + x[i]
    return S/n

n = 0
C = 1
while (C == 1):
    n = int (input("Numero de valores: "))
    if (2 < n <= 30):
        C = 0

A = Lee (n)
R = Prom (A)
print (" La lista A es: ", A)
print ("El promedio fue: ", R)

