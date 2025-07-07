from zombie import *
from ogre import *
from hero import *
from weapon import *


def battle(hero: Hero, enemy: Enemy) -> None:
    """
    Simulates a battle between a hero and an enemy.

    Both sides attack each other in turns until one's health drops to zero or below.
    The outcome is printed after the fight.

    Args:
        hero (Hero): The hero character.
        Enemy (Enemy): The enemy character.
    """
    while hero.health_points > 0 and enemy.health_points > 0:
        print('-------------')
        print(f'{hero.type_of_enemy}: {hero.health_points}')
        print(f'{enemy.type_of_enemy}: {enemy.health_points}')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
        print('-------------')

    if hero.health_points > 0:
        print(f'{hero.type_of_enemy} wins')
    elif enemy.health_points > 0:
        print(f'{enemy.type_of_enemy} wins')


hero = Hero(10, 1)
zombie = Zombie(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

battle(hero, zombie)