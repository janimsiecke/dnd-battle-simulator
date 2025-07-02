from core_data.creature_size import CreatureSize
from core_data.creature_type import CreatureType
from core_data.alignment import CreatureAlignmentLawfulChaotic
from core_data.alignment import CreatureAlignmentGoodEvil

from actors.base_actor import Actor
from actors.traits.base_trait import Trait

class Monster(Actor):
    traits: [Trait] or None

    def __init__(
            self,
            traits: [Trait] or None,
            name: str,
            size: CreatureSize = CreatureSize.MEDIUM,
            creature_type: CreatureType = CreatureType.OTHER,
            alignment: [CreatureAlignmentLawfulChaotic, CreatureAlignmentGoodEvil] or None = None,
            max_hp: int = 1,
            speed: int = 30,
            strength: int = 10,
            dexterity: int = 10,
            constitution: int = 10,
            intelligence: int = 10,
            wisdom: int = 10,
            charisma: int = 10,
    ):
        super().__init__(
            name,
            size,
            creature_type,
            alignment,
            max_hp,
            speed,
            strength,
            dexterity,
            constitution,
            intelligence,
            wisdom,
            charisma,
        )
        if traits:
            self.traits = traits