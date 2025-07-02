from enum import Enum

class AttackTypes(Enum):
    MELEE_WEAPON_ATTACK = 'melee weapon attack',
    RANGED_WEAPON_ATTACK = 'ranged weapon attack',
    MELEE_SPELL_ATTACK = 'melee spell attack',
    RANGED_SPELL_ATTACK = 'ranged spell attack',
    UNARMED_STRIKE = 'unarmed strike',
    NATURAL_WEAPON_ATTACK = 'natural weapon attack'
