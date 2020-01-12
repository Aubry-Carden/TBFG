import os
import random
from entities import Enemy
from functions import clear_screen, option_selector

def battle(player, ai_level):
    clear_screen()
    print("Prepare for battle!")
    enemy = Enemy(ai_level)
    check = False
    player_is_blocking = False
    result = None
    while not check:
        clear_screen()
        print(f'You are fighting a level {ai_level} enemy, it\'s remaining health is {enemy.hp}, your remaining health is {player.current_hp}hp!\n')
        print('-'*40)
        print("Options:")
        print("  1: Attack!")
        print("  2: Block")
        print("  3: Run!")
        option = option_selector(3)
        if option == 1:
            otpt = enemy.calculate_damage(player.attack_damage)
            print(f'You did {otpt["damage"]} damage! Your enemy is now at {otpt["hp"]}hp!')
        elif option == 2:
            player_is_blocking = True
        elif option == 3:
            print("You run away.. coward.")
            check = True
            result = "run"
        print('-'*20)

        if enemy.hp <= 0:
            check = True
            player.coins += ai_level*100
            player.xp += ai_level*10 + random.randint(1,50)
            player.current_hp = player.max_hp
            result = "won"
        else:
            otpt = player.calculate_damage(enemy.attack_damage, player_is_blocking)

        if player.current_hp <= 0:
            check=True
            player.current_hp = player.max_hp
            result = "loss"

    clear_screen()
    if result == "won":
        print("You won the battle!")
        player.wins += 1
    elif result == "loss":
        print("You lost the battle..")
        player.losses += 1
    elif result == "run":
        print("You ran away from battle!")
        player.losses += 1
    input("Press enter to continue...")

    return ["menu_request:main_menu", player]

def fight():
    option = False
    while not option:
        clear_screen()
        print("Options:")
        print("  1: Easy AI")
        print("  2: Medium AI")
        print("  3: Hard AI")
        print("  4: Extreme AI")
        print("  5: Custom AI")
        print("  6: Back")
        option = option_selector(6)
        if option != 6:
            if option == 5:
                check = False
                while not check:
                    try:
                        level = input("Enemy Level: ")
                        if level.isdigit():
                            level = int(level)
                            check = True
                        else:
                            level = None
                            check = False
                    except Exception as e:
                        pass
                return f'menu_request:battle {level}'
            else:
                return f'menu_request:battle {option}'
        else:
            return "menu_request:main_menu"

def store(player):
    finished = False
    while not finished:
        clear_screen()
        print("  1: Abilities")
        print("  2: Back")
        option = option_selector(2)
        if option == 1:
            check = False
            while not check:
                clear_screen()
                print(f"Player XP: {player.xp}")
                print("-"*10)
                print(f"Max hitpoints: {player.max_hp}")
                print(f"Attack Damage: {player.attack_damage}")
                print(f"Defensive ability: {player.defense_ablilty}")
                print("-"*10)
                print("Options:")
                print("  1: Increase max hitpoints by 10 (10 XP)")
                print("  2: Increase attack damage by 4 (10 XP)")
                print("  3: Increase defensive ability by 1 (2 XP)")
                print("  4: Back")
                option = option_selector(4)
                if option == 1:
                    if player.xp >= 10:
                        player.max_hp += 10
                        player.current_hp = player.max_hp
                        player.xp -= 10
                elif option == 2:
                    if player.xp >= 10:
                        player.attack_damage += 4
                        player.xp -= 10
                elif option == 3:
                    if player.xp >= 2:
                        player.defense_ablilty += 1
                        player.xp -= 2
                elif option == 4:
                    check = True
        elif option == 2:
            return ["menu_request:main_menu", player]



def main_menu():
    option = False
    while not option:
        clear_screen()
        print("Options:")
        print("  1: Fight!")
        print("  2: Store")
        print("  3: Save Character")
        print("  4: Load Character")
        print("  5: Exit")
        option = option_selector(5)
        if option == 1:
            option = "menu_request:fight"
        elif option == 2:
            option = "menu_request:store"
        elif option == 3:
            option = "action_request:save_character"
        elif option == 4:
            option = "action_request:load_character"
        elif option == 5:
            option = "action_request:exit_game"
    return option

def title():
    print("Turn Based Fighting Game by Thermixia#9183")
    print("-"*43)
    print("Upgrade your character, destory your enemy!")
    print("-"*43)
    input("Press Enter to Continue...")
