# Programa: Megawatts_w                 28/05/26
# Autor: Gazca Loria Dana Madai
# Objetivo: Manejo de archivos en disco y listas
# Problema: Generar un archivo en disco con los pronosticos de generacion
#      de capacidad eolica en Megawatts por año desde 2017 a 2031.
#      NOTA: Cuando la cantidad es cero(0) termina la informacion.
#            El nombre del archivo debe ser: Megawatts.dat
#      Los 15 datos por año son:
#          4329, 5505, 6957, 8050, 8050, 9444, 9800, 10170, 11601,
#          12627, 13640, 14581, 15602, 16388, 12233

archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Megawatts.dat", "w")

print("Introducir los pronosticos")
print("Desde el año 2017 a 2031")

year = 2017

while True:
    print("Año: " + str(year), end= " ")
    val = input("Cantidad: ")
    if val == '0':
        break
    archivo.write (val)
    archivo.write ("\n")
    year = year+1

archivo.close()
print ("\nArchivo: Megawatts.dat bien generado y cerrado")
print("\nProceso terminado")
