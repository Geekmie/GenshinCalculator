from element import *

class StatType(Enum):
    Empty = 0
    Atk = 1
    AtkR = 2
    Crit = 3
    CritDMG = 4
    Defs = 5
    DefsR = 6
    ElmMaster = 7
    EngRechrg = 8
    Hp = 9
    HpR = 10

class artifact:
    def __init__(self, name = "unknown"):
        self.name = name
        self.mainStat = StatType.Empty
        self.substats = [{StatType.Empty: 0}] * 4
    
    def print(self):
        print("artifact:")
        pprint.pprint(attrs(self))
