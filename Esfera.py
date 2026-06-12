# Programa: Esfera                         21/05/2026
# Autor: Gazca Loria Dana Madai
# Objetivo: Definición y uso de la clase (class) Esfera
# Problema: Leer el radio de una esfera y calcular
#      el volumen. Escribir los valores de Radio y Volumen.

import math

class Esfera:

    def fun1(self):
        r = float(input("Valor del radio = "))
        v = (4/3) * math.pi * r**3
        
        print("Radio =", r)
        print("Volumen =", v)

# EMPIEZA EL PROGRAMA

print("Enseguida se obtiene la instancia (copia) Esfera1 de Esfera")

Esfera1 = Esfera()
Esfera1.fun1()

print("\nProceso terminado")
