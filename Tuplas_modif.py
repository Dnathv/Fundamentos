# Programa: Tuplas_modif                            05.JUN.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso y aplicacion de tuplas.
#   El contenido de las tuplas se puede desempacar para (recuperar,
#   accesar, leer) y se aplica la siguiente sintaxis
#               (d1,d2,d3, ...) = nombre_tupla
# Problema: Generar la tupla "TD" con 4 datos.
#   Desempacarlos e indicar cual de los 4 se quiere modificar.
#   Con los cambios, generar y escribir la tupla TD2
# ¡¡¡NOTA: NO aplicar listas ni cadenas; ni las funciones: list, tuple!!!

print ("1.- Generar la tupla TD con la siguiente informacion:")
print ("Manuel, H, 25, Toluca")
TD = ("Manuel", "H", 25, "Toluca")
print ("La tupla TD tiene 4 datos")

print ("\n2.- La tupla se desempaca en 4 variables: d1, d2, d3, d4")

(d1, d2, d3, d4) = TD             #La TD se desempaca

Num = int(input("Que dato se va a modificar: 1, 2, 3, 4: "))
val = input("Nuevo valor = ")

if Num == 1:
    d1 = val
elif Num == 2:
    d2 = val
elif Num == 3:
    d3 = int(val)
else:
    d4 = val

print ("\n3.- Se vuelve a formar la tupla con los cambios")
TD2 = (d1, d2, d3, d4)
print (" Tupla inicial TD: ", TD)
print (" Nueva tupla TD2: ", TD2)

print ("\nProceso terminado")
