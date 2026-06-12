# Programa: Circulo1                            19/05/26 
# Autor: Gazca Loria Dana Madai
# Objetivo: Definición y uso de la clase círculo. Círculo
#      tiene 2 métodos __init__(self, radio) y area(self)
# Problema: Definir la clase círculo con constructor qué incluya como  
#      parámetro el radio y con ese valor se calcule el área del círculo. 
# Nota: Tomar en cuenta para obtener la instancia del círculo se debe
#      incluir el área. 
# Nota 2: Tomar en cuenta para obtener la instancia del círculo se debe
#      incluir el radio. 

from math import pi
class Circulo:
    def __init__(self, radio):
        self. radio=radio
    def area(self):
        x = (pi*(self. radio**2))
        return(x)

# Comienza Programa principal 
print("Calculo del área de un circulo")
r = float(input("Valor del radio:")) # 4.5
print("Se obtiene la instancia C de circulo")
C = Circulo(r)
x = C.area()
print("El área es:", x)
print("El area es: %7.3f"% x)
print("Proceso terminado")
