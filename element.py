from enum import Enum
from utils import *

class Element(Enum):
    Empty = 0
    Pyro = 1
    Hydro = 2
    Dendro = 3
    Electro = 4
    Anemo = 5
    Cryo = 6
    Geo = 7
    Physical = 8

class elementStats:
    def __init__(self):
        self.DMG = dict((val.name, 0) for val in Element)
        self.RES = self.DMG.copy()
    
    def print(self):
        print("element stats:")
        print(attrs(self))