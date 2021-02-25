import pygame as pg

from settings import LINE_WIDTH
from enums import ObjectId


class Cube(pg.sprite.Sprite):
    def __init__(self, surface, size, cords):
        super().__init__()
        self.surface = surface
        self.colour = (255, 255, 255)
        self.size = size
        self.type = ObjectId.CUBE
        self.wx, self.wy = cords
        self.x = self.wx * (self.size + LINE_WIDTH)
        self.y = self.wy * (self.size + LINE_WIDTH)

    def draw_me(self):
        pg.draw.rect(
            self.surface,
            self.colour,
            pg.Rect(self.x, self.y, self.size, self.size))

    # Получить координаты
    def get_cords(self):
        return self.x, self.y

    # Задать координаты
    def set_cords(self, x, y):
        self.x = x
        self.y = y

    # Получить координаты относительно игровой сетки
    def get_w_cords(self):
        return self.wx, self.wy

    # Задать координаты относительно игровой сетки
    def set_w_cords(self, wx, wy):
        self.wx = wx
        self.wy = wy
