# Programa: Prueba_if3                                      Feb/2026
# Autor: Daniel Barajas y Valencia
# Objetivo: Aplicar la herramienta de flujo de control "if". 
# Problema: Usar expresiones logicas compustas (and) con un "if/else"
#   para saber si el valor "M" que se introduce por el teclado
#   es multiplo de 3 y de 7.

print ("\nCalcular si M es multiplo de 3 y de 7\n")

M = int (input ("Introduce el valor entero de M: "))
if ( M%3==0 and M%7==0 ):
    print ("M SI es multiplo de 3 y 7")
else:
    print ("\nM NO es multiplo de 3 y 7")

print ("\nProceso terminado")
