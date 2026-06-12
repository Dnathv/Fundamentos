# Programa: Circulo2            19/05/26 
# Autor: Gazca Loria Dana Madai
# Objetivo: Definición y uso de la clase círculo. Círculo tiene
#      2 métodos __init__(self, radio) y area(self)
# Problema: Definir la clase círculo con constructor qué incluya
#      como parámetro el radio y con ese valor se calcule el área
#      del círculo. 
# Nota: Tomar en cuenta para obtener la instancia del círculo se
#      debe incluir el área. 
# Nota 2: Tomar en cuenta para obtener la instancia del círculo
#      se debe incluir el radio. 

from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    # Función para obtener el radio
    def get_radio(self):
        return self.radio

    # Función para calcular el área
    def area(self):
        return pi * (self.radio ** 2)

    # Función para calcular el perímetro
    def perimetro(self):
        return 2 * pi * self.radio

# Comienza Programa principal
print("Cálculo del área y perímetro de un círculo")
r = float(input("Valor del radio: "))  # Por ejemplo: 4.5

# Crear instancia de círculo
c = Circulo(r)

# Obtener radio, área y perímetro
radio = c.get_radio()
area = c.area()
perimetro = c.perimetro()

# Aumentamos el perímetro (ejemplo +10%)
perimetro_aumentado = perimetro * 1.10

# Imprimir resultados
print(f"Radio: {radio}")
print(f"Área: {area}")
print(f"Perímetro original: {perimetro}")
print(f"Perímetro aumentado: {perimetro_aumentado:.2f}")

print("Proceso terminado")
