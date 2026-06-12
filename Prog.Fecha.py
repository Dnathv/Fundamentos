# Programa: Fecha
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso de la clase "date time" y el modulo now()
#           tambien se aplica la funcion "getattr()"
#Problema: Obtener la fecha (anio, mes, dia)
#   Se requiere importar la clase "datetime"
#   La expresion: datetime.datetime.now()
#   retorna una lista con las variable llamadas:
#   ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
#   La funcion: getattr( ) tiene la siguiente sintaxis:
#               valor = getattr (lista, nombre)
#   retorna el valor de la variable "nombre" que se 

import datetime
print ('Fecha y Hora actual: ')
F = datetime.datetime.now()

A= getattr(F, 'year')
M= getattr(F, 'month')
D= getattr(F, 'day')
print ('Año = ',A)
print ('Mes = ',M)
print ('Dia = ',D)

print ("\nProceso Terminado") 
