import random

import xmltodict

xml_file = open("enemies.xml")
data = xml_file.read()
xml_file.close()

enemy_dict = xmltodict.parse(data)

enemies = enemy_dict['enemies']['enemy']
current_enemy_index = 0
enemy = enemies[current_enemy_index]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.potion_count = 2

    def attack(self, enemy):
        damage = random.randint(0, 40)
        enemy.health -= damage
        print("Has quitado {} puntos de vida al enemigo.".format(damage))

    def use_potion(self):
        if self.potion_count > 0:
            self.health += 50
            if self.health > 1000:
                self.health = 1000
            self.potion_count -= 1
            print("Has usado una poción. Tu salud actual es de {}. Te quedan {} pociones.".format(self.health, self.potion_count))
        else:
            print("No tienes pociones disponibles.")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.attack_power = 50

    def attack(self, player):
        damage = random.randint(0, self.attack_power)
        player.health -= damage
        print("El enemigo te ha quitado {} puntos de vida.".format(damage))

# Programa principal
player = Player("Jugador")
enemy = Enemy("Enemigo")

print("¡Bienvenido a Clash of Pythons!")
while True:
    action = input("¿Qué quieres hacer? (ataca/usar poción): ")
    if action == "ataca":
        player.attack(enemy)
        enemy.attack(player)
    elif action == "usar poción":
        player.use_potion()
    else:
        print("No entiendo esa acción. Inténtalo de nuevo.")
    
    if player.health <= 0:
        print("Has perdido.")
        break
    elif enemy.health <= 0:
        print("¡Has ganado!")
        break
