# Programa: ListaTempSlicing1                  30.Abr.26
# Autor: Gazca Loria Dana Madai

import math
import random

def Prom (x):
    S = 0
    for i in range (len (x)):
        S = S + x[i]
    return S/len (x)

n = int (input ("Numero de valores: "))
T = []
T1 = []
T2= []

for i in range (0,n):
    D = random.randint(5,30)
    T.append(D)

    if (i >= n/2):
        T2.append (T[i])
    else:
        T1.append (T[i])

print ("La lista T es: ",T)
print ("La lista T1 es: ",T1)
print ("La lista T2 es: ",T2)

ProT = Prom (T)
ProT1 = Prom (T1)
ProT2 = Prom (T2)

print ("El promedio de T es: ", ProT)
print ("El promedio de T1 es: ", ProT1)
print ("El promedio de T2 es: ", ProT2)

M = 0
if (ProT > ProT1 and ProT > ProT2):
    M = ProT
else:
    if (ProT1 > ProT and ProT1 > ProT2):
        M = ProT1
    else:
        M = ProT2

print ("El promedio mayor es: ",M)
    
print ('\nProceso terminado...')





