# Programa: Prueba_if1                                      Feb/2026
# Autor: Daniel Barajas y Valencia
# Objetivo: Aplicar la herramienta de flujo de control "if". 
# Problema: Usar expresiones logicas simples con un "if" para
#   diferentes problemas. 

A = int ( input("Valor de A: "))
if ( A < 0 ):
    A = A*(-1)
    print ("A Se cambio a positivo\n")

B = int ( input("Valor de B: ") )

if ( A > B ):
    print ("\nA es mayor que B")
    print ("Calculo de A-B ", str(A-B))

if ( A < B ) :
    print ("\nA es menor que B")

print ("\nProceso terminado")


