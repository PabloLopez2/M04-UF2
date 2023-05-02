#!/usr/bin/python3

import xmltodict

class Player:
	def __init__ (self, name, health=100, strength=10, level=1, xp=0):
		self.name = name
		self.health = health
		self.strength = strength
		self.level = level
		self.xp = xp

		xml_file = open("levels.xml", "r")

		levels = xmltodict.parse(xml_file.read())

		xml_file.close()

		tmp = levels["levels"]["level"]
		
		print(tmp)

		self.levels = {}

		for level in tmp:
			self.levels[ int(level["@num"]) ] = int(level["@xp"])


		print(self.levels)


	def set_health (self, health):
		self.health = health

	def set_strength (self, strength):
		self.strength = strength

	def set_level (self, level):
		self.level = level

	def get_level(self, xp):
		level_cur = self.level

		for level in self.levels:
			if self.levels[level] <= xp:
				level_cur = level

			return level_cur

	def set_xp (self, xp):
		self.xp = xp
	
	def hurt (self):

	def attack (self):
	



	def show_info (self):
		print("Name: "+self.name)
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))
		print("Level: "+str(self.level))
		print("XP: "+str(self.xp))

		
		
		
		
	
if __name__ == "__main__":
	player = Player("Juan Ramón")


