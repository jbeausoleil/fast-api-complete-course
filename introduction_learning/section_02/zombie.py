from random import random
from enemy import *

class Zombie(Enemy):
    """
    A class representing a Zombie enemy.

    Inherits from:
        Enemy: The base class for all enemy types.

    The Zombie can talk, attempt to spread disease, and use a regeneration special ability.
    """

    def __post_init__(self):
        """
        Post-initialization to set the specific enemy type for Zombie.
        """
        self._type_of_enemy = "Zombie"
        super().__post_init__()

    def talk(self):
        """
        Prints the Zombie's unique sound to simulate speech.
        """
        print(f'*Grumbling...*')

    def spread_disease(self):
        """
        Prints a message describing the Zombie's attempt to spread infection.
        """
        print(f'The {self.type_of_enemy} is trying to spread an infection.')

    def special_ability(self):
        """
        Tries to regenerate the Zombie's health by 2 points with a 50% chance.

        If regeneration occurs, prints a regeneration message.
        """
        did_special_ability_work = random() < 0.5
        if did_special_ability_work:
            self.health_points += 2
            print(f'{self.type_of_enemy} regenerates 2 HP.')