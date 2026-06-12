# Programa: IMC_Esp                       19.03.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Aplicacion de la estructura repetitiva "While"
# Problema: Generar e imprimir una lista que muestre la siguiente
#      informacion de "n" personas.
#      Nombre completo, Sexo, Edad, IMC, Esperanza de vida.
# Formulas: IMC = Peso/(Estatura * Estatura)
#           Esperanza: Hombres = 73 - Edad
#                      Mujeres = 78 - Edad
# Se nos proporciona la siguiente informacion:
#      Nombre, año de nacimiento, sexo, Peso, Estatura

import datetime
F = datetime.datetime.now()
A= getattr(F, 'year')

print ("Calculo del IMC y la Esperanza de vida\n")
n = int (input("Numero de personas: "))
contador = 0

while (contador < n):
    Nom  = input ("Nombre completo: ")
    ANac = int (input("Año de nacimiento: "))
    Sexo = input("Sexo (M o H): ")
    P    = float (input("Peso (Kg): "))
    Est  = float(input("Estatura : "))

    IMC = P/(Est*Est)

    Edad = A - ANac

    if (Sexo == 'M'):
        Esp = 78 - Edad
    if (Sexo == 'H'):
        Esp = 73 - Edad

    print ("{0:20}{1:3}{2:4d}{3:10.3f}{4:4d}".
           format(Nom, Sexo, Edad, IMC, Esp))

    contador = contador + 1

print ("\nProceso Terminado")
    
        
