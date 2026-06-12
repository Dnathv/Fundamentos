# Programa: Prueba_if4                                      Feb/2026
# Autor: Daniel Barajas y Valencia
# Objetivo: Aplicar la herramienta de flujo de control "if/elif/else". 
# Problema: Usar expresiones logicas compustas (or) con un "if/elif/else"
#   para evaluar si una calificacion es correcta (entre 0 y 10) y definir
#   si es Aprobado o No Aprobado.

Cal = int ( input("\nCalificion: "))
if (Cal > 10  or  Cal < 0):
    print ("Valor erroneo de la Calificacion")
    print ("  ¡¡Hacer la correccion !!  ")   
elif (Cal >= 6):
        print ("Aprobado ¡¡¡  :)")
else:
    print ("NO Aprobado")

print ("\nProceso Terminado")    
