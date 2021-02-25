from bot.cube import Cube
from enums import ObjectId


class Wall(Cube):
    def __init__(self, surface, size, cords):
        super().__init__(surface, size, cords)
        self.colour = (185, 55, 20)
        self.type = ObjectId.WALL
