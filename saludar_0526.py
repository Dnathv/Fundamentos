# Programa: saludar_0526.            12/05/26 
# Autor: Gazca Loria Dana Madai
# Objetivo: Aplicar PO sin constructor 
# Problema: Definir la clase (class) persona que incluya la función método saludar. Generar la instancia copia 
# copia Per1, aplicar la función/ método saludar. 

class Persona:
    def saludar(self):
        print("Les habla:")
        print("Hola esime zacatenco")
        print("Empezamos un nuevo tema")

# Comienza Programa principal 
print("Se genera la clase persona")  
input()  
print("Se genera la instancia o copia Per1 de la clase persona") 
print("Ahora vamos a trabajar con la clase Per1") 
Per1=Persona()
print("Se aplica la función/método saludar")
Per1.saludar()
print("Proceso terminado")