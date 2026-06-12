#Programa: Suma_n                      20.02.26
#Autor: Dana Madai Gazca Loria
#Objetivo: Aplicacion de la estructura repetitiva con in range
#Problema: Calcular e imprimir la suma y el promedio de "n"
#    valores enteros

print ("Uso de la estructura in range\n")

T = 0
n = int(input("Valor de n: "))

for x in range (n):
    dato = int(input ("Valor = "))
    T = T + dato
    
print ("Valor de la suma: ",T)
P = T/n
print ("Valor del promedio: ",P)

print("\nProceso terminado")
