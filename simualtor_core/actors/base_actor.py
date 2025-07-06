from core_data.dice import Dice, DiceSizes
from core_data.creature_size import CreatureSize
from core_data.creature_type import CreatureType
from core_data.alignment import CreatureAlignmentLawfulChaotic
from core_data.alignment import CreatureAlignmentGoodEvil
from core_data.damage_type import DamageType
from core_data.condition import Condition

from actors.traits.base_trait import Trait
from actors.actions.base_action import Action
from simualtor_core.game.sim_logging import LOGGER

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
    stats: dict
    stats_modifier: dict

    # Actions
    actions: [Action]

    # Traits
    traits: [Trait] or None

    # Damage Type Interactions
    damage_vulnerabilities: [DamageType] or None
    damage_resistances: [DamageType] or None
    damage_immunities: [DamageType] or None
    condition_immunities: [Condition] or None

    # Dynamic Values
    current_hp: int
    dead: bool

    def __init__(
            self,
            name: str,
            size: CreatureSize = CreatureSize.MEDIUM,
            creature_type: CreatureType = CreatureType.OTHER,  # noqa
            alignment:[CreatureAlignmentLawfulChaotic, CreatureAlignmentGoodEvil] or None = None,
            max_hp: int = 1,
            speed: int = 30,
            stats: dict or None = None,
            actions: [Action] or None = None,
            traits: [Trait] or None = None,
            damage_vulnerabilities: [DamageType] or None = None,
            damage_resistances: [DamageType] or None = None,
            damage_immunities: [DamageType] or None = None,
            condition_immunities: [Condition] or None = None,
    ):
        self.name = name
        self.size = size
        self.type = creature_type
        self.alignment = alignment
        self.max_hp = max_hp
        self.speed = speed
        if stats is None:
            self.stats = {
                "Strength": 10,
                "Dexterity": 10,
                "Constitution": 10,
                "Intelligence": 10,
                "Wisdom": 10,
                "Charisma": 10,
            }
        else:
            self.stats = stats
        self.__set_stat_modifiers()
        self.actions = actions
        self.traits = traits
        self.damage_vulnerabilities = damage_vulnerabilities,
        self.damage_resistances = damage_resistances,
        self.damage_immunities = damage_immunities,
        self.condition_immunities = condition_immunities,
        self.current_hp = self.max_hp
        self.dead = False

    def __set_stat_modifiers(self):
        self.stats_modifier = {}
        for stat in self.stats.keys():
            self.stats_modifier[stat] = (self.stats[stat] - 10) % 2

    def take_damage(self, damage_amount: int, damage_type: DamageType):
        if damage_type in self.damage_vulnerabilities:
            self.current_hp -= damage_amount * 2
        elif damage_type in self.damage_resistances:
            self.current_hp -= int(damage_amount / 2)
        elif damage_type in self.damage_immunities:
            pass
        else:
            self.current_hp -= damage_amount
        if self.current_hp <= 0:
            self.dead = True

    def is_dead(self):
        return self.dead

    def get_initiative(self):
        return Dice(DiceSizes.D20).roll() + self.stats_modifier['Dexterity']
