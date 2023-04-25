#!/usr/bin/python3

import xmltodict

title = "Editor de enemigos"

print(title)
print("-"*len(title))


def obten_datos ():
	name = input("Nombre: ")
	strength = int(input("Fuerza: "))
	health = int(input("Salud: "))
	
	return {
		"name": name,
		"damage": strength,
		"health": health
	}

def escribe_datos (export):
	enemy_xml = xmltodict.unparse(export, pretty=True)

	print(enemy_xml)

	archivo = open("enemies.xml", "w")

	archivo.write(enemy_xml)

	archivo.close()


salir = False
enemigos = []

while not salir:
	opcion = input("¿Quieres añadir un enemigo? [s/N]")

	if opcion != "s":
		salir = True
		continue

	
	enemigo = obten_datos()

	enemigos.append(enemigo)




enemies_export = {
	"enemies": {
		"enemy": enemigos
	}
}

escribe_datos(enemies_export)

