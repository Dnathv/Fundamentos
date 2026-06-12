# Programa: Try_excep_Intro2
# Autor: Gazca Loria Dana Madai
# Objetivo: Aplicar la estructura "try/exept" para analizar cuando
#      se tenga una raiz cuadrada negativa.
# Problema: Introducir los valores enteros de: a, d, c y calcular:
#      P = a+b-c
#      R = Raiz cuadrada

import math
print ("Calcular la raiz cuadrada de a*b-c")
a = int(input("Ingresar el valor de a: "))
b = int(input("Ingresar el valor de b: "))
c = int(input("Ingresar el valor de c: "))

try:
    P = a*b-c
    print ("El valor de P = a*b-c: ", P)
    R = math.sqrt(P)
    print ("La raiz cuadrada de P: ", R)
    
except:
    print ("Ocurrio un error")
    print ("Valor de a*b-c=", P)
    print ("No se puede calcular R, raiz negativa")
    R = 0

print ("Calculo de X = R+5")
x = R+5
print ("x = ", x)

print ("Proceso terminado")
