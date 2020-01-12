import platform
import json
import os
from entities import Player

def save_character(player):
    name = input("\nSave Name:")
    PlayerData = {
        "max_hp": player.max_hp,
        "current_hp": player.current_hp,
        "coins": player.coins,
        "xp": player.xp,
        "attack_damage": player.attack_damage,
        "defense_ablilty": player.defense_ablilty,
        "potions": player.potions
    }
    with open(f'PlayerSaves/{name}', 'w+') as f:
        json.dump(PlayerData, f, indent=4)
    del name, PlayerData
    return "menu_request:main_menu"

def load_character():
    files = os.listdir('./PlayerSaves')
    print("\nSaved Characters:")
    for counter, file in enumerate(files):
        print(f'  {counter+1}: {file}')
    character_number = option_selector(len(files))
    with open(f'PlayerSaves/{files[character_number-1]}') as f:
        PlayerData = json.load(f)
    player = Player(PlayerData["max_hp"], PlayerData["current_hp"], PlayerData["coins"], PlayerData["xp"], PlayerData["attack_damage"], PlayerData["defense_ablilty"])
    del files, character_number, PlayerData
    return ["menu_request:main_menu", player]

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def option_selector(max_int, min_int=1):
    try:
        option = input("\nSelect an Option: ")
        if option.isdigit():
            if min_int <= int(option) <= max_int:
                option = int(option)
            else:
                option = False
        else:
            option = False
    except Exception as e:
        print(e)
    finally:
        del min_int, max_int
        return option
