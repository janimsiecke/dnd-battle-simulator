from core_data.dice import DiceTray
from core_data.damage_type import DamageType
from core_data.attack_type import AttackTypes

class Action:
    name: str

    def __init__(self, name: str):
        self.name = name


class Attack(Action):
    attack_type: AttackTypes
    attack_range: int
    attack_bonus: int
    target_count: int
    damage_dice: [(DamageType, DiceTray, int)]

    def __init__(
            self,
            name: str,
            attack_type: AttackTypes,
            attack_range: int,
            attack_bonus: int,
            target_count: int,
            damage_dice: [(DamageType, DiceTray, int)]
    ):
        super().__init__(name)
        self.attack_type = attack_type
        self.attack_range = attack_range
        self.attack_bonus = attack_bonus
        self.target_count = target_count
        self.damage_dice = damage_dice
