from bot.cube import Cube
from enums import ObjectId


class Corpse(Cube):
    def __init__(self, surface, size, cords, energy):
        super().__init__(surface, size, cords)
        self.colour = (189, 189, 189)
        self.type = ObjectId.CORPSE
        self.energy = energy
