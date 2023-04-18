#!/usr/bin/python3
#Objeto que contiene la función read. (Se añade 1 salto de línea)
#read(8) escribe los 8 primeros carácteres.


#print(archivo.readline(8))
#Podemos ponerle delimitador

try:
	archivo = open("numeritos.txt", "r")
#print(archivo.readline())
	linea = archivo.readline()
	lista = linea.split(";")
	print(lista[3])
	archivo.close()
except:
	print("Error al abrir el archivo")

archivo.close()

archivo = open("textitos.txt", "w")

archivo.write("ola k ase")

archivo.close()

diccionario = {
	"nombre":"Guillem"
	"apellido":"Agulló"
	"lema": "ni oblit ni perdó"
	"altura":"1.1"
}

print(diccionaro[2])


