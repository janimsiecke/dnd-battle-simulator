from actors.actions.base_action import Attack
from core_data.dice import DiceTray, DiceSizes
from core_data.damage_type import DamageType
from core_data.attack_type import AttackTypes

MONSTER_ATTACK_LIBRARY = {
    "wolf_bite": Attack(
        "Bite",
        AttackTypes.MELEE_WEAPON_ATTACK,
        5,
        4,
        1,
        [(DamageType.PIERCING, DiceTray([DiceSizes.D4, 2]), 2)]
    )
}