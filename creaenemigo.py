#!/usr/bin/python3
#import pprint

import xmltodict

print("Crea un enemigo")
print("---------------")

#Por defecto input es str
name = input("Nombre: ")
strength = int(input("Fuerza: "))
health = int(input("Salud: "))

#Ahora hemos de transformar esto en un objeto 
#Diccionario = array con casillas
#Esto es un objeto (se parece a JSON): 
enemy = {
	"enemy": {
		"name": name,
		"damage": strength,
		"health": health
	}
}

#enemy["name"]

enemy_xml = xmltodict.unparse(enemy, pretty=True)

print(enemy_xml)

#Si no existe lo crea y escribe
archivo = open("enemy.xml", "w") 
archivo.write(enemy_xml)
archivo.close











