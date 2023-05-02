#!/usr/bin/python3

import xmltodict

from enemy_class import Enemy

class Enemies:
	def __init__(self):
		xml_file = open("enemies.xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())

		enemies_list = enemies_tmp['enemies']['enemy']

		self.enemies = []

		for e in enemies_list:
			#tmp = Enemy(e["name"], e["health"], e["damage"], "TEST")

			self.enemies.append(Enemy(e["name"], e["health"], e["damage"]))

			


if __name__ == "__main__":
	enemies = Enemies()
