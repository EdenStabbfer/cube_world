import pygame as pg
from settings import SHIFT


class Grid:
    def __init__(self, width, height, line_width, cell_size, bg_colour):
        super().__init__()
        self.width = width
        self.height = height
        self.world_width = width // (cell_size + line_width) + 1
        self.world_height = height // (cell_size + line_width) + 1
        self.line_w = line_width
        self.cell_size = cell_size

        self.bg_colour = bg_colour

    # Генерирует сетку из ниний
    def lines_generate(self):
        surface = pg.surface.Surface((self.width, self.height), pg.SRCALPHA)
        surface.fill(self.bg_colour)
        for i in range(self.world_width):
            x = (i + 1) * self.cell_size + i * self.line_w + (self.line_w - 1) // 2
            pg.draw.line(surface, (50, 55, 60), (x, 0), (x, self.height), self.line_w)

        for j in range(self.world_height):
            y = (j + 1) * self.cell_size + j * self.line_w + (self.line_w - 1) // 2
            pg.draw.line(surface, (50, 55, 60), (0, y), (self.width, y), self.line_w)
        return surface

    # Возращает отмасштабированный размер главного окна
    def get_adj_size(self):
        width = self.world_width*(self.cell_size + self.line_w) - self.line_w
        height = self.world_height*(self.cell_size + self.line_w) - self.line_w
        return width, height

    # Возвращает размер сетки
    def get_world_size(self):
        return self.world_width, self.world_height
