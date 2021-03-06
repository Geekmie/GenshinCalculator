
from element import *

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
        pprint.pprint(attrs(self))


class advancedStats:
    def __init__(self):
        self.crit = 0
        self.critDMG = 0
        self.heal = 0
        self.incomeHeal = 0
        self.engRechrg = 0
        self.reduceCD = 0
        self.powerShield = 0

    def print(self):
        print("advanced stats:")
        pprint.pprint(attrs(self))

class buffs:
    def __init__(self):
        self.atkSpeed = 0
        self.allDMG = 0
        self.NormalAtkDMG = 0
        self.ChargedAtkDMG = 0
        self.ChargedAtkCrit = 0
        self.PlungingDMG = 0
        self.SkillDMG = 0
        self.BurstDMG = 0
        self.SwirlDMG = 0
        self.OverloadedDMG = 0
        self.ElectrochargedDMG = 0
        self.SuperconductDMG = 0
        self.BurningDMG = 0
        self.VaporizeDMG = 0
        self.MeltDMG = 0

    def print(self):
        print("buffs:")
        pprint.pprint(attrs(self))

class normalAtk:
    def __init__(self):
        self.hits = [] # 1~6
        self.chargeAtk = [] # 1, 2
        self.plunges = [] # plunge, low, high

    def print(self):
        print("normal attack:")
        pprint.pprint(attrs(self))


class skill:
    def __init__(self):
        self.DMG = []

    def print(self):
        print("skill:")
        pprint.pprint(attrs(self))


class burst:
    def __init__(self):
        self.DMG = []
        self.engCost = 0
    
    def print(self):
        print("burst:")
        pprint.pprint(attrs(self))


class character:
    def __init__(self, name):

        self.name = name
        self.elementType = Element.Empty

        # Levels
        self.level = 1
        self.attackLvl = 1
        self.skillLvl = 1
        self.burstLvl = 1
        self.constellation = 1

        # Stats
        self.baseStats = baseStats()
        self.advancedStats = advancedStats()
        self.buffs = buffs()
        self.elementStats = elementStats()

        # Skills
        self.normalAtk = normalAtk()
        self.skill = skill()
        self.burst = burst()


    def print(self):
        print(self.name)
        pprint.pprint(attrs(self))
        self.baseStats.print()
        self.advancedStats.print()
        self.buffs.print()
        self.elementStats.print()
        self.normalAtk.print()
        self.skill.print()
        self.burst.print()