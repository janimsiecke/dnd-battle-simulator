from core_data.creature_size import CreatureSize
from core_data.creature_type import CreatureType
from core_data.alignment import CreatureAlignmentLawfulChaotic
from core_data.alignment import CreatureAlignmentGoodEvil

from actors.actions.base_action import Action

class Actor:
    # Name and Typing
    name: str = ""
    size: CreatureSize
    creature_type: CreatureType
    alignment: [CreatureAlignmentLawfulChaotic, CreatureAlignmentGoodEvil] or None = None

    # Basics
    max_hp: int
    speed: int

    # Stats
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    # Actions
    actions: [Action]

    # Dynamic Values
    current_hp: int

    def __init__(
            self,
            name: str,
            size: CreatureSize = CreatureSize.MEDIUM,
            creature_type: CreatureType = CreatureType.OTHER,  # noqa
            alignment:[CreatureAlignmentLawfulChaotic, CreatureAlignmentGoodEvil] or None = None,
            max_hp: int = 1,
            speed: int = 30,
            strength: int = 10,
            dexterity: int = 10,
            constitution: int = 10,
            intelligence: int = 10,
            wisdom: int = 10,
            charisma: int = 10
    ):
        self.name = name
        self.size = size
        self.type = creature_type
        self.alignment = alignment
        self.max_hp = max_hp
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.current_hp = self.max_hp