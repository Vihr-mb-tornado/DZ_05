from character import Character
from student import Student

def attack_message(attacker: Character, target: Character, damage_done: float) :
    return f'{attacker.name} атакував {target.name}.\n' \
           f'{attacker.name} наніс {damage_done} шкоди. ' \
           f'У {target.name} залишилося {target.health} здоров`я.'


player1 = Character('Vasya', 100, 15, 25)
player2 = Character('Petya', 100, 20, 12)

print(f'Створено нового персонажа: {player1.name}')
print(f'Створено нового персонажа: {player2.name}')

player1.show_stats()
player2.show_stats()
count = 0
while player1.is_alive() and player2.is_alive():
    count = count + 1
    damage_done = player1.attack(player2)
    #print(attack_message(player1, player2, damage_done))

    damage_done = player2.attack(player1)
    #print(attack_message(player2, player1, damage_done))

print(f'Обмін ударів :{count}')
print(f'{player1}\n{player2}')


student1 = Student('Stepan', 2006, "В21958", 11)
student1.show_stats()
print(f'Вік студента: {student1.get_age()}')