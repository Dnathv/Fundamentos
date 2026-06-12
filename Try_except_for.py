# Programa: try_except_ for
# Autor: Gazca Loria Dana Madai
# Objetivo: Aplicacion del try except dentro de un ciclo for.
# Problema: Definir la lista numeros [5, -8, 0, 12] los valores de
#     las listas separadas por comas y leer el valor de x para obtener
#     e imprimir el resultado de x / numeros, obtener e imprimir  la 
#     suma de los resultados.

print ("Numeros = [5, -8, 0. 12]")
numeros = [5, -8, 0, 12]
suma = 0
x = int(input("Valor de x: "))

for n in numeros:
    try:
        calculo = x/n
        print ("El valor de ", x,"Entre ", n,"=", calculo)
        suma = suma + calculo
    except:
        print ("No se puede dividir entre 0")

print ("La suma de los calculos es {0:8.2f}".format(suma))
print ("Proceso terminado")
