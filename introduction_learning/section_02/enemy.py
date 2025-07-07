from dataclasses import dataclass, asdict, field

@dataclass
class Enemy:
    """
    Base class for enemy characters in the game.

    Attributes:
        _type_of_enemy (str): Internal string indicating the enemy's type.
        health_points (int): The enemy's current health.
        attack_damage (int): The base attack damage the enemy can inflict.
    """
    _type_of_enemy: str = field(init=False, default="unknown")
    health_points: int = 10
    attack_damage: int = 1

    def __post_init__(self):
        """
        Initialization hook called after the dataclass has been created.
        Ensures the enemy type is set; raises an error if not.
        """
        if not self._type_of_enemy:
            raise ValueError("Enemy type cannot be empty.")

    @property
    def type_of_enemy(self) -> str:
        """
        Provides read-only access to the enemy type.

        Returns:
            str: The enemy's type as a string.
        """
        return self._type_of_enemy

    def talk(self) -> None:
        """
        Prints a basic line introducing the enemy and warning the player.
        """
        print(f'I am a {self.type_of_enemy}. Be prepared to fight.')

    def walk_forward(self) -> None:
        """
        Prints a message indicating the enemy is moving closer to the player.
        """
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self) -> None:
        """
        Prints the enemy's attack action and the amount of damage dealt.
        """
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage.')

    def special_ability(self) -> None:
        """
        Prints a message indicating that the enemy has no special ability.
        Intended to be overridden by subclasses that have special abilities.
        """
        print(f'{self.type_of_enemy} has no special ability.')