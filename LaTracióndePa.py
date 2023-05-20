#!/usr/bin/python3
import random
import xmltodict
import json
import cowsay

class Enemy:
    def __init__(self, name, damage, health, description):
        self.name = name
        self.damage = damage
        self.health = health
        self.description = description

class Player:
    def __init__(self):
        self.health = 1450
        self.experience = 0
        self.level = 1
        self.potion_count = 2

    def use_potion(self):
        if self.potion_count > 0:
            self.health += 50
            if self.health > 1000:
                self.health = 1000
            self.potion_count -= 1
            print("Has usado una poción. Te sube 50 de vida. Tu salud actual es de " + str(self.health) + ". Te quedan " + str(self.potion_count) + " pociones.")
        else:
            print("No tienes pociones disponibles.")

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("El enemigo te ha quitado " + str(damage) + " puntos de vida.")


class Game:
    def __init__(self):
        self.enemies = []
        self.current_enemy_index = 0
        self.player = Player()

    def load_enemies_from_xml(self, filename):
        xml_file = open(filename)
        data = xml_file.read()
        xml_file.close()

        enemy_dict = xmltodict.parse(data)
        enemy_data = enemy_dict['enemies']['enemy']

        for enemy_info in enemy_data:
            name = enemy_info['name']
            damage = int(enemy_info['damage'])
            health = int(enemy_info['health'])
            description = enemy_info['description']

            enemy = Enemy(name, damage, health, description)
            self.enemies.append(enemy)

    def show_game_over_message(self):
        message = "Has perdido papu, fin de la partida. No hay checkpoints así que no te queda otra que empezar desde 0."
        cowsay.cow(message)

    def show_enemy_defeated_message(self):
        message_enemy_defeat = "Has derrotado al enemigo. ¡Felicidades!"
        cowsay.cow(message_enemy_defeat)

    def show_game_completed_message(self):
        message_completed_game = "¡Has completado el juego! ¡Enhorabuena por demostrar que la justicia no siempre gana!"
        cowsay.cow(message_completed_game)

    def start(self):
        print("\n*** ¡BIENVENIDO AL JUEGO: LA TRAICIÓN DE PABLO! ***\n")
        print("\nContexto: Todo comienza un día donde Pablo traiciona a su clase, miente en su beneficio, oculta y roba a sus compañeros en secreto, pero un día fue descubierto, entonces los compañeros decidirán sentenciarlo a muerte y lucharán contra él.")

        load_option = input("¿Quieres cargar la partida guardada? (si/no) ")
        if load_option.lower() == "si":
            load_format = input("¿En qué formato está guardada la partida? (xml/json) ")
            load_filename = input("Introduce el nombre del archivo de partida: ")

            if load_format.lower() == "xml":
                self.load_game_xml(load_filename)
            elif load_format.lower() == "json":
                self.load_game_json(load_filename)
            else:
                print("Formato de partida no válido. Iniciando nueva partida.")


        while True:
            enemy = self.enemies[self.current_enemy_index]

            COLOR_RED = '\033[91m'
            COLOR_YELLOW = '\033[93m'
            COLOR_GREEN = '\033[92m'
            COLOR_RESET = '\033[0m'

            #Colores enemigo
            if enemy.health > 100:
                health_color = COLOR_GREEN
            elif enemy.health > 50:
                health_color = COLOR_YELLOW
            else:
                health_color = COLOR_RED

            #Colores Jugador
            if self.player.health >= 800:
                player_health_color = COLOR_GREEN
            elif self.player.health >= 300:
                player_health_color = COLOR_YELLOW
            else:
                player_health_color = COLOR_RED

            print("\n=== INFO ENEMIGO ===")
            print("+------------------------+")
            print("| Nombre:      {}{:9}{} |".format(COLOR_RED, enemy.name, COLOR_RESET))
            print("| Daño:        {}{:9}{} |".format(COLOR_RED, enemy.damage, COLOR_RESET))
            print("| Salud:       {}{:9}{} |".format(health_color, enemy.health, COLOR_RESET))
            print("+------------------------+")
            print("Descripción: " + str(enemy.description))

            print("\n=== STATS DE PABLO ===")
            print("+------------------------+")
            print("| Salud:       {}{:9}{} |".format(player_health_color, self.player.health, COLOR_RESET))
            print("| Nivel:       {:9} |".format(self.player.level))
            print("| Experiencia: {:9} |".format(self.player.experience))
            print("| Pociones:    {:9} |".format(self.player.potion_count))
            print("+------------------------+")

            action = input("¿Qué quieres hacer? (ataca/nada/poción/guardar_partida/exit) ")

            if action == "ataca":
                damage = random.randint(0, 40)
                enemy.health -= damage
                print("Has quitado " + str(damage) + " puntos de vida al enemigo.")
                
            elif action == "poción":
                self.player.use_potion()

            elif action == "guardar_partida":
                save_format = input("¿En qué formato deseas guardar la partida? (xml/json) ")
                save_filename = input("Introduce el nombre del archivo de guardado: ")

                if save_format.lower() == "xml":
                    self.save_game_xml(save_filename)
                elif save_format.lower() == "json":
                    self.save_game_json(save_filename)
                else:
                    print("Formato de guardado no válido.")

            elif action == "exit":
                print("¡Hasta la próxima!")
                break

            else:
                print("Te quedas mirando las musarañas.")

            player_damage = enemy.damage - random.randint(0, 5)
            self.player.receive_damage(player_damage)

            if enemy.health <= 0:
                self.player.experience += 50
                self.player.level = self.player.experience // 100 + 1

                self.show_enemy_defeated_message()

                self.current_enemy_index += 1
                if self.current_enemy_index >= len(self.enemies):
                    self.show_game_completed_message()
                    break
                else:
                    enemy = self.enemies[self.current_enemy_index]
                    enemy.damage += (self.player.level - 1) * 10
                    enemy.health += (self.player.level - 1) * 50
                    print("El enemigo ha subido de fuerza.")

            if self.player.health <= 0:
                self.show_game_over_message()
                break


    def save_game_xml(self, filename):
        data = {
            'current_enemy_index': self.current_enemy_index,
            'enemy_health': self.enemies[self.current_enemy_index].health,
            'player_health': self.player.health,
            'player_experience': self.player.experience,
            'player_level': self.player.level,
            'potion_count': self.player.potion_count
        }

        xml_data = xmltodict.unparse({'game': data}, pretty=True)
        with open(filename, 'w') as xml_file:
            xml_file.write(xml_data)
        print("Partida guardada en XML correctamente.")

    def load_game_xml(self, filename):
        with open(filename, 'r') as xml_file:
            data = xml_file.read()
        game_data = xmltodict.parse(data)['game']
        
        self.current_enemy_index = int(game_data['current_enemy_index'])
        self.enemies[self.current_enemy_index].health = int(game_data['enemy_health'])
        self.player.health = int(game_data['player_health'])
        self.player.damage = 0
        self.player.level = int(game_data['player_level'])
        self.player.experience = int(game_data['player_experience'])
        print("Partida cargada desde XML correctamente.")

    def save_game_json(self, filename):
        data = {
            'current_enemy_index': self.current_enemy_index,
            'enemy_health': self.enemies[self.current_enemy_index].health,
            'player_health': self.player.health,
            'player_damage': 0,
            'player_level': self.player.level,
            'player_experience': self.player.experience
        }
        
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Partida guardada en JSON correctamente.")

    def load_game_json(self, filename):
        with open(filename, 'r') as json_file:
            game_data = json.load(json_file)
        
        self.current_enemy_index = int(game_data['current_enemy_index'])
        self.enemies[self.current_enemy_index].health = int(game_data['enemy_health'])
        self.player.health = int(game_data['player_health'])
        self.player.damage = int(game_data['player_damage'])
        self.player.level = int(game_data['player_level'])
        self.player.experience = int(game_data['player_experience'])
        print("Partida cargada desde JSON correctamente.")

# Crear una instancia del juego y ejecutarlo
game = Game()
game.load_enemies_from_xml("enemies.xml")
game.start()

