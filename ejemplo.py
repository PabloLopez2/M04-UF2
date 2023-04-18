print("ola k ase")                                                                                                                    

#Funciones
def suma_numeros (a, b):
	print(a + b)

#Variables
num1 = 8
num2 = 12

#Condiciones
if num1 > num2:
	print("Es Mayor")
elif num1 < num2:
	print("Es Menor")
else:
	print("Son iguales")

#Concatenar la string con el número, str transforma lo que le pasemos en string.
frase = "Queréis correr y no sabéis ni la base"
print(frase+str(num1))

#Bucles
contador = 10
while contador > 0:
	print(contador)
	contador -= 1

frutas = ["peras", "cerezas", "manzanas", "melocotones"]
for fruta in frutas:
	print(fruta)

teclado = input("Introduce tu nombre: ")
print("Hola "+teclado+"\nxd")
#print(int(teclado+7)) Por si pasamos un entero y queremos sumarlo

#Lista o Arrays
#Se pueden mezclar tipos en las listas
lista = [1, 2, "tres", 4]
#La función te retorna el número de casillas que tiene una array
#Una string es una array de carácteres 
print(len(lista[2])) 

suma_numeros(num1, num2)

