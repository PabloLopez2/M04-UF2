#!/usr/bin/python3

import random

class Enemy:
	def __init__(self, name, health, strength, description = ""):
		self.name = name
		self.health = health
		self.strength = strength
		self.description = description

		print(self.name+": "+self.description)

	def attack (self):
		return random.randint(0, self.strength)

	def show_info (self):
		print("Name: "+self.name)
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))

		if self.description != "":
			print("Description: "+self.description)
	
	def hurt(self, damage):
		self.health -= damage

		if self.health > 0:
			return False
		
		return True
			
		


if __name__ == "__main__":
	enemigo = Enemy("Jacinto", 33, 10, "Es un bicho feo")

	enemigo.show_info()

	print(enemigo.attack())
