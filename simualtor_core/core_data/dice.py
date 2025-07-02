from enum import Enum
from random import randint

class DiceSizes(Enum):
    D2 = 2,
    D4 = 4,
    D6 = 6,
    D8 = 8,
    D10 = 10,
    D12 = 12,
    D20 = 20,
    D100 = 100

class Dice:
    name: str
    size: int

    def __init__(self, dice: DiceSizes):
        self.name = dice.name
        self.size = dice.value[0]

    def roll(self, advantage: bool = False, disadvantage: bool = False):
        if advantage:
            if disadvantage:
                return self.__roll()
            return max(self.__roll(), self.__roll())
        if disadvantage:
            return min(self.__roll(), self.__roll())
        return self.__roll()

    def __roll(self):
        return randint(1, self.size)

class DiceTray:
    dice = [(Dice, int)]

    def __init__(self, dice: [(DiceSizes, int)]):
        self.dice = dice

    def roll_all(self, advantage: bool = False, disadvantage: bool = False):
        total: int = 0
        for dice in self.dice:
            for _ in range(dice[1]):
                total += dice[0].roll(advantage, disadvantage)
        return total
