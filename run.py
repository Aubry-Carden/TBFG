import menus
from entities import Player
from functions import clear_screen, save_character, load_character
import json

with open('config.json', 'r') as f:
    config = json.load(f)

clear_screen()
if config["DevMode"] == True: player = Player(max_hp=999, current_hp=999, coins=9999, xp=9999, attack_damage=200, defense_ablilty=2000)
else: player = Player()
del config
menus.title()

# Start main loop
while True:
    instruction = menus.main_menu()
    while instruction != "main_menu":
        if instruction.startswith("menu_request:"):
            instruction = instruction[len("menu_request:"):len(instruction)]
            if instruction == "fight":
                instruction = menus.fight()
            elif instruction.startswith("battle"):
                instruction = instruction[len("battle "):len(instruction)]
                instruction = menus.battle(player, int(instruction))
                player = instruction[1]
                instruction = instruction[0]
            if instruction == "store":
                instruction = menus.store(player)
                player = instruction[1]
                instruction = instruction[0]
        elif instruction.startswith("action_request:"):
            instruction = instruction[len("action_request:"):len(instruction)]
            if instruction == "save_character":
                instruction = save_character(player)
            elif instruction == "load_character":
                instruction = load_character()
                player = instruction[1]
                instruction = instruction[0]
            elif instruction == "exit_game":
                clear_screen()
                print("Thanks for playing!\n")
                exit(0)
