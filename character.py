﻿import random
class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0
    damage_offset = 0.2

    def __init__(self, name, health, damage, defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def show_stats(self):
        print(self)

    def __str__(self):
        return f' -< {self.name} >- \n' \
            f' Здоров`я: {self.health}\n'\
            f' Шкода: {self.damage}\n'\
            f' Захист: {self.defence}\n'

    def take_damage(self, damage):
        real_offset = random.randint(0, int(damage * self.damage_offset)) * random.choice((-1,1))
        real_damage = round(max( damage * ((100 - self.defence) / 100) + real_offset,0),2)
        #if (self.defence > 100):
        #    real_damage = 0
        self.health = round(max(self.health - real_damage, 0),2)
        return real_damage

    def attack(self, target):
        return target.take_damage(self.damage)

    def is_alive(self):
        if self.health>0:
            return True
        else:
            return False



