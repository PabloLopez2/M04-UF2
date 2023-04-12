import random
import math
num_max = 100


azar = math.floor(random.random()*100)+1
salir = False

print("¡JUEGO ADIVINA EL NÚMERO!")

while not salir:
	num = int(input("Introduce un número del 1 al "+str(num_max)+": "))
	if num < azar:
		print("El número es menor")
	elif num > azar:
		print("El número es mayor")
	else:
		print("ADIVINIASTE COMPANYY")
		salir = True



