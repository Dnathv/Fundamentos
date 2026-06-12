# Programa: Autos_25_r                 28/05/26
# Autor: Gazca Loria Dana Madai
# Objetivo: Manejo de archivos en disco
# Problema: Leer la informacion anual de autos fabricados guardada en
#      el archivo "Autos_25.dat" y escribir la informacion y la suma
#      acumulada por año.

archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Autos_25.dat", "r")

print("Numero de autos fabricados")
print("Cantidad Suma acumulada")

suma = 0

for auto in archivo:
    auto = int(auto)
    suma = suma + auto
    print ("{0:6}{1:10}". format (auto, suma))

archivo.close()
print("\nProceso terminado")
