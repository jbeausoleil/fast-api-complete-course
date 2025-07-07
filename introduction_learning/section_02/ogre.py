from enemy import *
from random import random

class Ogre(Enemy):
    """
    A class representing an Ogre enemy.

    Inherits from:
        Enemy: The base class for all enemy types.

    The Ogre can talk and use a special ability to increase its health points.
    """

    def __post_init__(self):
        """
        Post-initialization to set the specific enemy type for Ogre.
        """
        self._type_of_enemy = "Hero"
        super().__post_init__()

    def talk(self):
        """
        Prints the Ogre's unique action to simulate speech.
        """
        print(f'The {self.type_of_enemy} is slamming hands all around.')

    def special_ability(self):
        """
        Has a 20% chance to increase the Ogre's health points by 4.

        If the ability is successful, prints a notification message.
        """
        did_special_ability_work = random() < 0.2
        if did_special_ability_work:
            self.health_points += 4
            print(f'{self.type_of_enemy} attack has increased by 4.')