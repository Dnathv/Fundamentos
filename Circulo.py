# Programa: Circulo                            18/05/26 
# Autor: Gazca Loria Dana Madai
# Objetivo: Definición y uso de la clase (class) Calc_r
# Problema: Definir la clase sin constructor, pero tiene la función fun1,
#     la cual debe de leer los valores A, B y calcular R (R=sqrt+A**B)
#     escribir los valores de A, B, R. 

import math
class Calc_r:
    def fun1(self):
        A = int(input("Valor de A:"))
        B = int(input("Valor de B:"))
        R = math.sqrt(A**B)
        print("A, B, r")
        print("{0:5d} {1:5d} {2:8.4f}".format(A, B, R))
        

# Comienza Programa principal 
print("En seguida se obtiene la instancia (copia) Calc1 de Calc_r")
Calc1=Calc_r()
Calc1.fun1()
print("Proceso terminado")
