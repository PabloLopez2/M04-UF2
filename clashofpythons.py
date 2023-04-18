import xmltodict
import random

#Cargar los archivos
enemy_files = ["enemy1.xml", "enemy2.xml", "enemy3.xml"]
enemy_file = random.choice(enemy_files)

with open(enemy_file, "r") as f:
    xml_string = f.read()

# Conviertir el archivo XML a un diccionario de Python
enemy_dict = xmltodict.parse(xml_string)

#Definir valores del archivo XML
name = enemy_dict["enemy"]["name"]
description = enemy_dict["enemy"]["description"]
health = int(enemy_dict["enemy"]["health"])
strength = int(enemy_dict["enemy"]["strength"])

#Mi vida
player_health = 20

#Bucle
while True:
    # Mostrar información del enemigo
    print(f"\n{name}: {description}")
    print(f"Health: {health}, Strength: {strength}")

    #acción
    action = input("¿Qué quieres hacer? (ataca/nothing)")

    if action == "ataca":
        damage = random.randint(0, 5)
        health -= damage
        print(f"Has quitado {damage} puntos de vida al enemigo.")
    else:
        print("Te quedas mirando las musarañas")

    #El enemigo me pega o no
    player_damage = random.randint(0, 2)
    player_health -= player_damage
    print(f"El enemigo te ha quitado {player_damage} puntos de vida.")

	#Saluf enemigo
    if health <= 0:
        print("Acabaste con él. ¡Felicidades!")
        break
    
	#Mi salud
    if player_health <= 0:
        print("Mala suerte papu, has perdido.")
        break


#print(diccionario)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(diccionario)

#print(diccionario["characters"]["character"][0]["name"])

#character_num = int(input("Introduce un número del 1 al 4: ")) - 1

#character = diccionario["characters"]["character"][character_num]

#print("Nombre: "+character["name"])
#print("Salud: "+character["health"])
#print("DaÃ±o: "+character["damage"])
#print("Nivel: "+character["level"])
