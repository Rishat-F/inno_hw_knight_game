import random


monster_counter = 0
hp = 10
attack = 10


def create_monster():
    monster_hp = random.randint(8, 14)
    monster_attack = random.randint(6, 10)
    return 'monster', monster_hp, monster_attack


def create_apple():
    apple_hp = random.randint(3, 7)
    return 'apple', apple_hp


def create_sword():
    sword_attack = random.randint(6, 13)
    return 'sword', sword_attack


def random_meeting(*args):
    meeting = random.choice(args)
    return meeting()


def game():
    global monster_counter
    global hp
    global attack
    while hp > 0 and monster_counter < 10:
        meeting = random_meeting(create_monster, create_apple, create_sword)
        if meeting[0] == 'apple':
            hp_boost = meeting[1]
            hp += hp_boost
            print(f'\nВы нашли яблоко и съели его.\n'
                  f'Кол-во единиц здоровья увеличилось на {hp_boost}.\n'
                  f'Ваше текущее здоровье составляет {hp} ед.')
        elif meeting[0] == 'sword':
            sword_attack = meeting[1]
            print(f'\nВы нашли MEЧ, который дает {sword_attack} ед. урона.\n'
                  f'Ваша текущая атака составляет {attack} ед. урона.')
            choice = input(
                '\nЧтобы заменить свой старый меч на новый, введите 1.\n'
                'Чтобы оставить свой старый меч, введите 2.\n'
                )
            while True:
                if choice == '2':
                    print(f'\nВы оставили свой старый меч с '
                          f'атакой в {attack} ед. урона.')
                    break
                elif choice == '1':
                    attack = sword_attack
                    print(f'\nВы взяли новый меч и ваша атака теперь '
                          f'составляет {attack} ед. урона.')
                    break
                else:
                    choice = input(
                        '\nНекорректный ввод.\nВведите 1, чтобы заменить свой '
                        'старый меч на новый.\n'
                        'Введите 2, чтобы оставить свой старый меч.\n'
                        )
        else:
            monster_hp = meeting[1]
            monster_attack = meeting[2]
            print(f'\nБОЙ! На вас напало чудовище с {monster_hp} ед. '
                f'здоровья и с атакой в {monster_attack} ед. урона.\n'
                f'Ваше текущее здоровье составляет {hp} ед.\n'
                f'Ваша атака составляет {attack} ед. урона.')
            choice = input(
                '\nВведите 1, чтобы вступить в схватку с чудовищем.\n'
                'Введите 2, чтобы убежать.\n'
                )
            while True:
                if choice == '1':
                    print('\nВы вступили в схватку с чудовищем!')
                    while hp > 0 and monster_hp > 0:
                        hp -= monster_attack
                        monster_hp -= attack
                    if hp > 0:
                        monster_counter += 1
                        if monster_counter != 10:
                            print(
                                f'\nВы одолели чудовище! Но оно оставило вам '
                                f'{hp} ед. здоровья.\nЧтобы спасти '
                                f'Королевство осталось одолеть еще '
                                f'{10 - monster_counter} чудовищ.'
                                )
                    break
                elif choice == '2':
                    print('\nВы убежали.')
                    break
                else:
                    choice = input(
                        '\nНекорректный ввод.\nВведите 1, чтобы вступить '
                        'в схватку с чудовищем.\n'
                        'Введите 2, чтобы убежать.\n'
                        )
    if hp <= 0:
        print('\nМонстр вас убил. ПОРАЖЕНИЕ!\n\nИгра окончена.\n')
    else:
        print(
            '\nПОБЕДА!\nВы одолели 10 чудовищ и спасли '
            'Королевство от уничтожения!\n\nИгра окончена.\n'
            )
    monster_counter = 0
    hp = 10
    attack = 10
    quit()


if __name__ == '__main__':
    game()
