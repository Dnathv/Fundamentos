# Programa: Factorial_1
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicar la estructura repetitiva for i in range
# Problema: Calcular e imprimir el factorial de un numero entero y positivo
#       F = 1 * 2 * 3 * 4 * 5 * ..... * n

print ("Calculo del factorial de un numero.")
n = int(input("Ingrese un numero entero y positivo: "))

if (n<=0):
    print("\nFactorial = 1")
else:
    F = 1
    for i in range (1, n+1):
        F = F + i
        print(F, end = " ")
    print (f"\nEl factorial es = (0:10d)". format(F))
    #print(f"\n Factorial de (n) = (F)")

print ("Proceso terminado")
