from weapon import *
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Hero:
    """
    A class representing a hero character in the game.
    The hero can equip weapons and engage in battle with enemies.

    Attributes:
        _type_of_enemy (str): Internal identifier for the character type, always "Hero"
        health_points (int): Current health points of the hero
        attack_damage (int): Base attack damage without weapons
        weapon (Optional[Weapon]): Currently held weapon, if any
        is_weapon_equipped (bool): Tracks if the held weapon is equipped
    """
    _type_of_enemy: str = field(init=False, default="Hero")
    health_points: int
    attack_damage: int
    weapon: Optional[Weapon] = None
    is_weapon_equipped: bool = False

    @property
    def type_of_enemy(self) -> str:
        """
        Property providing read-only access to the hero type.
        
        Returns:
            str: The type of the character ("Hero")
        """
        return self._type_of_enemy

    def equip_weapon(self) -> None:
        """
        Equips the currently held weapon if one exists and isn't yet equipped.
        When equipped, the weapon's attack increase is added to the hero's attack damage.
        """
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True

    def attack(self) -> None:
        """
        Performs an attack action, displaying the total damage dealt.
        The damage includes both base attack damage and any equipped weapon bonus.
        """
        print(f'Hero attacks for {self.attack_damage} damage.')