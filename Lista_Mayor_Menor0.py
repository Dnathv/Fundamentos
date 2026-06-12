# Programa: Lista_Mayor_Menor0                                 Feb/2026
# Autor: Dana Madai Gazca Loria 
# Objetivo: Uso de listas de numeros enteros y aplicaciones de las funciones 
#   de ususario: Lee() y Imp()
# Problema: Definir la lista "A" y leer los "n" numeros que la componen.
#   Encontar el valor mayor de la lista "A" y escribirlo.
#   Generar y escribir la lista "B" que tendra el mayor de "A" dividido
#   entre los valores de "A"
#   Generar y escribir la lista "C" que tendra los valores de "A" divididos
#   entre el menor de "A" 

def Lee (n):
    L = []
    for i in range (0, n):
        valor = int(input("Valor # " + str(i+1) + ":"))
        L.append (valor)
    return L

def Imp (L):           
    for i in L:
        print ('{0:7.2f}'.format (i), end = " ")

A = []
n = int (input("Numero de elementos: "))

A = Lee (n)
print (" La lista A es: ", A)

ma = A[0]
for n in A:
    if n > ma:
        ma = n
print (f"El mayor de A es: {ma}")

me = A[0]
for n in A:
    if n < me:
        me = n
print (f"El menor de A es: {me}")

B = []
for i in A:
    B. append (ma/i)
print ("La lista B es: ",B)

C = []
for i in A:
    C. append (i/me)
print ("La lista B es: ",B)

print ("fin")





        
    










