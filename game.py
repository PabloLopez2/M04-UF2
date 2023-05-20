#!/usr/bin/python3

from enemies_class import Enemies
from player_class import Player

player = Player()

if __name__ == "__main__":
	title = "Empiesa el juego"
	print(title)
	print("-"*len(title))
	

	opc = ""
	while opc != "s":
		print("1.- Juego nuevo")
		print("2.- Cargar juego")
		print("S.- Salir")

		opc = input("Introduce una opción: ").lower()

		if opc == "1":
			player.input_info()
