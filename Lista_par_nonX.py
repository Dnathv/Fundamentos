# Programa: Lista_par_nonX                               16.Abr.26
# Autor: Dana Madai Gazca Loria 
# Objetivo: Uso de las funciones:  append();  
# Problema: Leer los "n" valores enteros de la lista "A" y escribirla;
#   Con los valores de la lista "A", generar dos lista (Par y Non);
#   en la lista Par quedaran los valores pares y en la lista Non
#   quedaran los valores nones.

A = []                                     # lista vacia
Par = []
Non = []
n = int (input("Numero de valores: "))

for i in range (n):
    x = int (input("Ingrese el valor: "))
    A.append(x)

    if (x%2==0):
        Par.append(x)
    else:
        Non.append(x)

print ("\nLa lista A es: ", (A))
print ("\nLa lista Par de valores pares es: ", (Par))
print ("\nLa lista Non de valores nones es: ", (Non) )

print ("\nProceso terminado. Oprima una tecla.")



