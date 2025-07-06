from core_data.creature_size import CreatureSize
from core_data.creature_type import CreatureType
from simualtor_core.actors.base_actor import Actor
from simualtor_core.actors.traits.base_trait import Trait
from simualtor_core.actors.actions.monster_attack_library import MONSTER_ATTACK_LIBRARY

MONSTER_LIBRARY = {
    "wolf": Actor(
        "Wolf",
        CreatureSize.MEDIUM,
        CreatureType.BEAST,
        None,
        max_hp=11,
        speed=40,
        stats={
            "Strength": 12,
            "Dexterity": 15,
            "Constitution": 12,
            "Intelligence": 3,
            "Wisdom": 12,
            "Charisma": 6
        },
        actions=['wolf_bite']
    )
}