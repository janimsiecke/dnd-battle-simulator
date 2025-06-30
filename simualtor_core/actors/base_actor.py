from core_data.size import CreatureSize
from core_data.type import CreatureType
from core_data.alignment import CreatureAlignmentLawfulChaotic
from core_data.alignment import CreatureAlignmentGoodEvil

class Actor:
    # Name and Typing
    name: str = ""
    size: CreatureSize
    type: CreatureType
    alignment: [CreatureAlignmentLawfulChaotic, CreatureAlignmentGoodEvil]

    # Basics
    max_hp: int
    hit_dice_size: int
    speed: int

    # Stats
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    # Dynamic Values
    current_hp: int

    def __init__(
            self,
            name: str,
            size: CreatureSize = CreatureSize.MEDIUM,
            type: CreatureType = CreatureType.OTHER,  # noqa
            alignment=None,
            max_hp: int = 1,
            hit_dice_size: int = 6,
            speed: int = 30,
            strength: int = 10,
            dexterity: int = 10,
            constitution: int = 10,
            intelligence: int = 10,
            wisdom: int = 10,
            charisma: int = 10
    ):
        if alignment is None:
            self.alignment = [
                CreatureAlignmentLawfulChaotic.NEUTRAL, CreatureAlignmentGoodEvil.NEUTRAL
            ]
        self.name = name
        self.size = size
        self.type = type
        self.max_hp = max_hp
        self.hit_dice_size = hit_dice_size
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.current_hp = self.max_hp