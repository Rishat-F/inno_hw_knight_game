import os
import random
import typing


monster_counter = 0
hp = 10
attack = 10


def greeting() -> bool:
    """Create greeting prompt for the player.

    Returns:
        Boolean depending on whether the player wants to start the game.
    """
    os.system("cls")
    print(
        '\nДобро пожаловать в сказочную игру "Герой и Монстры"!\n\n'
        "Королевству угрожает нападение со стороны 10 монстров!\n"
        "Лишь отважные и сильные способны спасти Королевство...\n"
    )
    choice = input("Готовы бросить вызов опасности? [y/n]\n").lower()
    while choice not in ("y", "n", "yes", "no", "\n", ""):
        choice = input('\nВведите "y" или "no" чтобы продолжить игру:\n')
    if choice.startswith("y") or choice in ("\n", ""):
        return True
    return False


def pretty_print() -> None:
    """Print stats and game steps in pretty view."""
    os.system("cls")
    print(
        f"----------------------------------------------\n"
        f"hp: {hp}   attack: {attack}   monsters_counter: {10 - monster_counter}\n"
        f"----------------------------------------------"
    )


def create_monster() -> typing.Tuple[str, int, int]:
    """Create a monster.

    Returns:
        A tuple containing 'monster' string, monster hp and monster attack.
        For example:

        ('monster', 10, 5)
        It means that monster has 10 hp and his attack is equal 5.
    """
    monster_hp = random.randint(6, 11)
    monster_attack = random.randint(5, 9)
    return "monster", monster_hp, monster_attack


def create_apple() -> typing.Tuple[str, int]:
    """Create an apple.

    Returns:
        A tuple containing 'apple' string and hp.
        For example:

        ('apple', 5)
        It means that 'apple' will restore 5 hp.
    """
    apple_hp = random.randint(3, 7)
    return "apple", apple_hp


def create_sword() -> typing.Tuple[str, int]:
    """Create a sword.

    Returns:
        A tuple containing 'sword' string and sword attack.
        For example:

        ('sword', 11)
        It means that 'sword' has attack equal to 11.
    """
    sword_attack = random.randint(6, 13)
    return "sword", sword_attack


def random_meeting() -> tuple:
    """Randomly define what object a hero would meet on next step.

    Returns:
        A new monster or an apple or a sword.
    """
    meeting = random.choice([create_monster, create_apple, create_sword])
    return meeting()


def game() -> None:
    """Define game logic.

    Call this function to start the game.
    """
    global monster_counter
    global hp
    global attack
    while hp > 0 and monster_counter < 10:
        input("\n\tНажмите ENTER, чтобы перейти к следующему ходу\n")
        pretty_print()
        meeting = random_meeting()
        if meeting[0] == "apple":
            hp_boost = meeting[1]
            hp += hp_boost
            pretty_print()
            print(
                f"\nВы нашли яблоко и съели его.\n"
                f"Кол-во единиц здоровья увеличилось на {hp_boost}."
            )
        elif meeting[0] == "sword":
            sword_attack = meeting[1]
            print(f"\nВы нашли MEЧ, который дает {sword_attack} ед. урона.")
            choice = input(
                "\n\tЧтобы заменить свой старый меч на новый, введите 1.\n"
                "\tЧтобы оставить свой старый меч, введите 2.\n"
            )
            while True:
                if choice == "2":
                    pretty_print()
                    print("\nВы оставили свой старый меч.")
                    break
                elif choice == "1":
                    attack = sword_attack
                    pretty_print()
                    print("\nВы подобрали новый меч.")
                    break
                else:
                    choice = input(
                        "\nНекорректный ввод.\n\tВведите 1, чтобы заменить "
                        "свой старый меч на новый.\n"
                        "\tВведите 2, чтобы оставить свой старый меч.\n"
                    )
        else:
            monster_hp = meeting[1]
            monster_attack = meeting[2]
            print(
                f"\nБОЙ! На вас напало чудовище с {monster_hp} ед. "
                f"здоровья и с атакой в {monster_attack} ед. урона."
            )
            choice = input(
                "\n\tВведите 1, чтобы вступить в схватку с чудовищем.\n"
                "\tВведите 2, чтобы убежать.\n"
            )
            while True:
                if choice == "1":
                    while hp > 0 and monster_hp > 0:
                        hp -= monster_attack
                        monster_hp -= attack
                    if hp > 0:
                        monster_counter += 1
                        if monster_counter != 10:
                            pretty_print()
                            print("\nВы одолели чудовище!")
                    break
                elif choice == "2":
                    pretty_print()
                    print("\nВы убежали.")
                    break
                else:
                    choice = input(
                        "\nНекорректный ввод.\n\tВведите 1, чтобы вступить "
                        "в схватку с чудовищем.\n"
                        "\tВведите 2, чтобы убежать.\n"
                    )
    if hp <= 0:
        pretty_print()
        print("\nМонстр вас убил. ПОРАЖЕНИЕ!\n\nИгра окончена.\n")
    else:
        pretty_print()
        print(
            "\nПОБЕДА!\nВы одолели 10 чудовищ и спасли "
            "Королевство от уничтожения!\n\nИгра окончена.\n"
        )
    monster_counter = 0
    hp = 10
    attack = 10
    quit()


if __name__ == "__main__":
    if greeting():
        pretty_print()
        print("\nИгра началась, удачи!")
        game()
    else:
        os.system("cls")
        print(
            "\nМного смельчаков пало в битве с монстрами...\n"
            "Но никто не смог остановить их.\n"
            "В итоге Королевство было разрушено чудовищами...\n\n"
            "Вы проиграли!\n\n"
            "Игра окончена."
        )
