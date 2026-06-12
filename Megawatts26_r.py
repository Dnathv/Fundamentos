# Programa: Megawatts26_r                                    29/05/26
# Autor: Gazca Loria Dana Madai
# Objetivo: Manejo de archivos en disco.
# Problema: Listar los pronosticos de generacion de Megawatts por año  
#       desde 2017 a la fecha guardados en el archivo "Megawatts.dat"     
#       Definir el numero de años "T" que se van a procesar.
#       Se debe obtener un reporte que tenga:
#           Año, Megawatts Variacion y Porcentaje.
#       Se recomienda generar una lista [mw] con las cantidades de mw y
#       otras dos con las variaciones [var] y porcentajes [porc].

archivo = open("E:/Fundamentos de Programacion/GLDM_Ficheros/Datos/Megawatts.dat", 'r')

print("Pronosticos de Generacion de Megawatts:")
print("Desde el año 2017 a la fecha")
year = 2017
T = int(input("Num de años a procesar (max 15): "))

            # Listas Vacias
var = []
porc = []
mw = []

# Se lee el archivo y se genera la lista mw[]
for Pronostico in archivo:
    valor = Pronostico
    valor = int(valor)
    mw.append(valor)
    
# El primer año, var y porc son cero.
var.append(0)
porc.append(0)

for i in range (1, T):
    var.append(mw[i] - mw[i-1])
    porc.append(var[i]/mw[i]*100)

print ("\n Año    Cantidad    Variacion    Porcentaje")
for i in range (0,T):
    print ("{0:5d}{1:10d}{2:10d}{3:12.2f}".
           format (year, mw[i], var[i], porc[i]))
    year = year+1

archivo.close()
print("\nProceso terminado")
