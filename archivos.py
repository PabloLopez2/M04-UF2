#!/usr/bin/python3
#Objeto que contiene la función read. (Se añade 1 salto de línea)
#read(8) escribe los 8 primeros carácteres.

archivo = open("numeritos.txt", "r")

#print(archivo.readline(8))

#Podemos ponerle delimitador
linea = archivo.readline()
lista = linea.split(";")
print(lista[2])

archivo.close()

archivo = open("textitos.txt", "w")

archivo.write("ola k ase")

archivo.close()



