# Programa: Fac_Fun                        12.Marzo.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Definicion de funcion con retorno de resultado.
# Problema: Definir la funcion "FactR" que calcule y retorne el resultado
#      de un numero entero y positivo.
#      Por definicon valor cero o negativo es igual a 1.

def FactR(n):
    if (n <= 0):
        return (1)
    else:
        F = 1
        for i in range(1, n+1):
            F = F * i
        return (F)

#Comienza el programa principal
print ("\nCalculo y retorno del factorial de un numero\n")
n = int(input("Valor de n: "))
R = FactR (n)
print ("El factorial del numero ingresado es: ", R)
print (f"Factorial de {n} = {R}")

print ("\nProceso terminado")
