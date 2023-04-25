import math
import random

DEBUG = True

num_max = 100
print("ADIVINA UN NÚMERO DEL 1 AL "+str(num_max))

azar = math.floor(random.random()*num_max)+1

if DEBUG:
	print("Numero al azar: "+str(azar))

salir = False

while not salir:
	num = int(input("Introduce un número del 1 al "+str(num_max)+": "))

	if num > azar:
		print("El número introducido es mayor")
	elif num < azar:
		print("El número introducido es menor")
	else:
		print("¡Acertaste!")
		salir = True
