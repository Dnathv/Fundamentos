# Programa: Read_Listas1.
# Autor: Dana Madai Gazca Loria
# Objetivo: Definición y uso de archivos de disco.
#      Se aplican las funciones: open, write, close, list, map, split.
#      Por ejemplo: clas = list(map(int, datos.split())).
#        split: Separa la cadena datos en subcadenas.
#        map: convierte las cadenas en enteros (int).
#        list: forma la lista cals.
# Problema: lee la información "Listas1" y ejecutar la modificación que se pide.

print("Abrir el archivo listas1 y ejecutar lo siguiente")
print("Si la primer calificación es menor a 6, modificarla a 6")
archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Listas1.dat", "r")

for datos in archivo:
    print("\nDatos Originales: ", datos, end=" ")
    cals = list(map(int, datos.split()))
    if cals[1] < 6:
        cals[1] = 6
    print("Calificaciones Modificadas: ", cals)

    Calf = cals[1:]
    Promd = sum (Calf)/len (Calf)
    print(f" Promedio: {Promd:.2f}")    
    
archivo.close()
    
print("Proceso terminado")
