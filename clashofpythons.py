#!/usr/bin/python3

import xmltodict
#import pprint

xml_file = open("clashofclans.xml", "r")

diccionario = xmltodict.parse(xml_file.read())

#print(diccionario)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(diccionario)

#print(diccionario["characters"]["character"][0]["name"])

character_num = int(input("Introduce un número del 1 al 4: ")) - 1

character = diccionario["characters"]["character"][character_num]

print("Nombre: "+character["name"])
print("Salud: "+character["health"])
print("Daño: "+character["damage"])
print("Nivel: "+character["level"])
