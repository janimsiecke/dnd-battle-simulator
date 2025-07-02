from core_data.creature_size import CreatureSize
from core_data.creature_type import CreatureType
from simualtor_core.actors.monster import Monster
from simualtor_core.actors.traits.base_trait import Trait

MONSTER_LIBRARY = {
    "wolf": Monster(
        [],
        "Wolf",
        CreatureSize.MEDIUM,
        CreatureType.BEAST,
        None,
        max_hp=11,
        speed=40,
        strength=12,
        dexterity=15,
        constitution=12,
        intelligence=3,
        wisdom=12,
        charisma=6
    )
}