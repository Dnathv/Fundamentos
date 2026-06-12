# Programa: Write_Listas1.
# Autor: Dana Madai Gazca Loria
# Objetivo: Definición y uso de archivos.
#    Se aplican las funciones: open(), write(), close().
# Problema: Generar le fichero "Listas1" con "n" casos que deben incluir:
#    Número de boleta y dos calificaciones.

archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Listas1.dat", "w")

n = int(input("Nuḿero de casos = "))
for i in range(n):
    bol = input("Introducir boleta: ")
    archivo.write(bol+" ")
    C1 = input("Calificación 1: ")
    archivo.write(C1+" ")
    C2 = input("Calificación 2: ")
    archivo.write(C2+" ")
    C3 = input("Calificación 3: ")
    archivo.write(C1+" ")
    C4 = input("Calificación 4: ")
    archivo.write(C2+" ")
    archivo.write("\n")
archivo.close()

print("\nProceso terminado")
