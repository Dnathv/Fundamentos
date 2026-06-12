# Programa: Factorial_2                        12.Marzo.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Definir y aplicar la funcion "Fact"
# Problema: Calcular e imprimir el factorial de un numero entero y positivo
#       F = 1 * 2 * 3 * 4 * 5 * ..... * n
# Nota: "Fact" Calcula e imprime el factorial

def Fact(n):
    if (n <= 0):
        F = 1
        print("\nFactorial = 1")
    else:
        F = 1
        for i in range (1, n+1):
            F = F * i
            print (F, end = " ")
    print (f"\nFactorial de {n} = {F}")

#Comienza el programa principal1
print ("Calculo del factorial de un numero")
n = int(input("Valor de n: "))
Fact(n)
print ("Proceso terminado")
input("");
