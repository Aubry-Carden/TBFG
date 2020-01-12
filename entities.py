import random

class Player():
    def __init__(self, max_hp=100, current_hp=100, coins=0, xp=0, attack_damage=10, defense_ablilty=1, wins=0, loses=0):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.coins = coins
        self.xp = xp
        self.attack_damage = attack_damage
        self.defense_ablilty = defense_ablilty
        self.wins = wins
        self.loses = loses


    def calculate_damage(self, attack_strenght, blocking):
        damage = round(attack_strenght / self.defense_ablilty)
        damage += random.randint(0,10)
        if damage > attack_strenght:
            damage = attack_strenght
        if random.randint(1,100) <= 1:
            damage = attack_strenght
        if blocking == True:
            damage -= self.attack_damage
        if damage < 0:
            damage = 0
        self.current_hp -= damage
        del attack_strenght, blocking
        return {
            "hp": self.current_hp,
            "damage": damage
        }

class Enemy():
    def __init__(self, level=0):
        self.hp = 0
        self.attack_damage = 0
        self.defense_ablilty = 0

        xp_to_spend = level*20
        subject = 1
        while xp_to_spend > 0:
            if xp_to_spend > 3:
                number = random.randint(round(xp_to_spend/6), round(xp_to_spend/2))
            else:
                number = xp_to_spend
            xp_to_spend -= number
            if subject == 1:
                self.hp += number
            elif subject == 2:
                self.attack_damage += number
            elif subject == 3:
                self.defense_ablilty += number
            subject += 1
            if subject > 3:
                subject = 0

        self.hp = self.hp*8
        self.attack_damage = self.attack_damage*2
        del xp_to_spend, subject, number

    def calculate_damage(self, attack_strenght):
        damage = round(attack_strenght / self.defense_ablilty)
        damage += random.randint(0,10)
        if damage > attack_strenght:
            damage = attack_strenght
        if random.randint(1,100) <= 1:
            damage = attack_strenght
        self.hp -= damage
        del attack_strenght
        return {
            "hp": self.hp,
            "damage": damage
        }
