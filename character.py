
from utils import *


class baseStats:
    def __init__(self):
        # Values
        self.hp = 0
        self.atk = 0
        self.defs = 0
        self.elemMaster = 0
        self.stamina = 0
        # Rates
        self.hpR = 0
        self.atkR = 0
        self.defsR = 0

    def print(self):
        print("base stats:")
        print(attrs(self))

class character:
    def __init__(self, name):

        self.name = name

        # Levels
        self.level = 1
        self.attackLvl = 1
        self.skillLvl = 1
        self.burstLvl = 1
        self.constellation = 1

        # Base stats
        self.baseStats = baseStats()

    def print(self):
        print(self.name)
        
        print(attrs(self))
        self.baseStats.print()
        