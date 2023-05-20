#!/usr/bin/python3
import random
import xmltodict

xml_file = open("enemies.xml")
data = xml_file.read()
xml_file.close()

enemy_dict = xmltodict.parse(data)

enemies = enemy_dict['enemies']['enemy']
current_enemy_index = 0
enemy = enemies[current_enemy_index]

#Vida del jugador, experiencia, nivel y poción
player_health = 1500
player_experience = 0
player_level = 1
potion_count = 2

print("INTRODUCCIÓN AL JUEGO: La traición de Pablo ")

print("\nContexto: Todo comienza un día donde Pablo traiciona a su clase, miente en su beneficio, oculta y roba a sus compañeros en secreto, pero un día fue descubierto, entonces los compañeros decidirán sentenciarlo a muerte y lucharán contra él.")

while True:
	#Muestro stats del enemigo
	print("\nNombre: " + str(enemy['name']))
	print("Daño: " + str(enemy['damage']))
	print("Salud: " + str(enemy['health']))
	print("Descripción: " + str(enemy['description']))

	#Mi vida, nivel y experiencia
	print("\nTu salud: " + str(player_health))
	print("Tu nivel maribel: " + str(player_level))
	print("Tu experiencia: " + str(player_experience))
	
	action = input("¿Qué quieres hacer? (ataca/nada/poción) ")

	# Pego o no
	if action == "ataca":
		damage = random.randint(0, 40)
		enemy['health'] = int(enemy['health']) - damage
		print("Has quitado " + str(damage) + " puntos de vida al enemigo.")
			
	elif action == "pocion":
		if potion_count > 0:
			player_health += 50
			if player_health > 1000:
				player_health = 1000
			potion_count -= 1
			print("Has usado una poción. Te sube 50 de vida. Tu salud actual es de " + str(player_health) + ". Te quedan " + str(potion_count) + " pociones.")
		else:
			print("No tienes pociones disponibles.")
		
	else:
		print("Te quedas mirando las musarañas.")

	#El enemigo me pega
	player_damage = int(enemy['damage']) - random.randint(0, 5)
	player_health = player_health - player_damage
	print("El enemigo te ha quitado " + str(player_damage) + " puntos de vida.")

	#Si acabamos con el enemigo
	if int(enemy['health']) <= 0:
		#Gano experiencia y subo de nivel
		player_experience += 50
		player_level = int(player_experience / 100) + 1

		print("Has derrotado al enemigo. ¡Felicidades!")
		#Seleccionar el siguiente enemigo del archivo XML
		current_enemy_index += 1
		if current_enemy_index >= len(enemies):
			#Te pasas el juego
			print("¡Has completado el juego! Enhorabuena por demostrar que la justícia no siempre gana.")
			break
		else:
			enemy = enemies[current_enemy_index]
			enemy['damage'] = int(enemy['damage']) + (player_level - 1) * 10
			enemy['health'] = int(enemy['health']) + (player_level - 1) * 50
			print("El enemigo ha subido de fuerza.")

	#Game over
	if player_health <= 0:
		print("Has perdido papu, fin de la partida. No hay checkpoints así que no te queda otra que empezar desde 0.")
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
