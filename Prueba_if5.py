# Programa: Prueba_if5                                      26.Feb.2026
# Autor: Daniel Barajas y Valencia
# Objetivo: Aplicar la herramienta de flujo de control "if/elif/else". 
# Problema: Usar expresiones logicas con un "if/elif/else"
#   para evaluar si un numero es positivo, negativo o cero.
#   Ademas calcular su cuadrado.

num = int (input ("\nIntroduzca un numero entero: "))
if ( num > 0 ):
    print("El numeero es positivo.")
elif ( num < 0 ):
    print("El numero es negativo.")
else:
    print("El numero es cero.")

print ("Cuadrado del numero = " '{0:8d}'.format(num*num))

print ("\nProceso terminado")
