# Programa: Autos_25_w                 26/05/26
# Autor: Gazca Loria Dana Madai
# Objetivo: Manejo de archivos en disco
# Problema: Generar un archivo en disco con los cantidades de autos fabricados anualmente desde el
#      2010 hasta la fecha.
#      Cuando la cantidad es cero, termina la información.

archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Autos_25.dat", "w")

print("Introducir la clase de autos producidos")
print("Desde el año 2010 hasta la fecha")
year = 2010

while True:
    print("Año: ", str(year))
    val = int(input("Cantidad: "))
    if val == 0:
        break
    val = str(val)
    archivo.write (val)
    archivo.write ("\n")
    year = year+1

archivo.close()
print("Proceso terminado")
