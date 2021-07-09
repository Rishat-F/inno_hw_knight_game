import random


monster_counter = 10
hp = 10
attack = 10


def create_monster():
    monster_hp = random.randint(6, 15)
    monster_attack = random.randint(3, 10)
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
    while hp > 0 and monster_counter > 0:
        meeting = random_meeting(create_monster, create_apple, create_sword)
        if meeting[0] == 'apple':
            hp_boost = meeting[1]
            hp += hp_boost
            print(f'Вы нашли яблоко и съели его.\n'
                  f'Кол-во единиц здоровья увеличилось на {hp_boost}.\n'
                  f'Ваше текущее здоровье составляет {hp} ед.\n')
        elif meeting[0] == 'sword':
            sword_attack = meeting[1]
            _input = input(
                f'Вы нашли МЕЧ, который дает {sword_attack} ед. урона.\n'
                f'Ваша текущая атака составляет {attack} ед. урона.\n'
                f'Чтобы заменить свой старый меч на новый, введите 1.\n'
                f'Чтобы оставить свой старый меч, введите 2.\n'
                )
            while True:
                if _input == '2':
                    print(f'Вы оставили свой старый меч с '
                          f'атакой в {attack} ед. урона.\n')
                    break
                elif _input == '1':
                    attack = sword_attack
                    print(f'Вы взяли новый меч и ваша атака теперь '
                          f'составляет {attack} ед. урона.\n')
                    break
                else:
                    _input = input('Некорректный ввод.\nВведите 1, чтобы '
                                   'заменить свой старый меч на новый.\n'
                                   'Введите 2, чтобы оставить '
                                   'свой старый меч.\n')
        else:
            monster_hp = meeting[1]
            monster_attack = meeting[2]
            _input = input(
                f'БОЙ! На вас напало чудовище с {monster_hp} ед. '
                f'здоровья и с атакой в {monster_attack} ед. урона.\n'
                f'Ваше текущее здоровье составляет {hp} ед.\n'
                f'Ваша атака составляет {attack} ед. урона.\n'
                f'Введите 1, чтобы вступить в схватку с чудовищем.\n'
                f'Введите 2, чтобы убежать.\n'
                )
            while True:
                if _input == '1':
                    print('Вы вступили в схватку с чудовищем!\n')
                    while hp > 0 and monster_hp > 0:
                        hp -= monster_attack
                        monster_hp -= attack
                    if hp <= 0:
                        print('Монстр вас убил. ПОРАЖЕНИЕ!\n'
                              'Игра окончена.')
                        break
                    elif monster_hp <= 0:
                        monster_counter -= 1
                        if monster_counter:
                            print(
                                f'Вы одолели чудовище! Но оно оставило вам '
                                f'{hp} ед. здоровья.\nЧтобы спасти '
                                f'Королевство осталось одолеть еще '
                                f'{monster_counter} чудовищ.\n'
                                )
                        else:
                            print(
                                'ПОБЕДА!\nВы одолели 10 чудовищ и спасли '
                                'Королевство от уничтожения!\nИгра окончена.\n'
                                )
                    break
                elif _input == '2':
                    print('Вы убежали.\n')
                    break
                else:
                    _input = input(
                        'Некорректный ввод.\nВведите 1, чтобы заменить свой '
                        'старый меч на новый.\nВведите 2, чтобы оставить '
                        'свой старый меч.\n'
                        )


if __name__ == '__main__':
    game()
