# Programa: Hora
#









import datetime
print ('Se obtendra la hora actual\n ')
C = datetime.datetime.now()

H= getattr(C, 'hour')
M= getattr(C, 'minute')
S= getattr(C, 'second')
print ('Hora = ',H)
print ('Minuto = ',M)
print ('Segundo = ',S)

print ('Hora actual:',H,':',M,':',S)

print ("\nProceso Terminado") 
