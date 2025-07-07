from dataclasses import dataclass

@dataclass
class Weapon:
    """
    Represents a weapon that can be equipped by a character to increase attack power.

    Attributes:
        weapon_type (str): The type or name of the weapon.
        attack_increase (int): The amount of additional attack damage this weapon provides (default is 0).
    """
    weapon_type: str
    attack_increase: int = 0