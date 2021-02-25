import pygame as pg
pg.font.init()

# Главные настройки
WIDTH = 1298
HEIGHT = 804
CUBE_SIZE = 50
LINE_WIDTH = 2
HEADER_HEIGHT = 60
FOOTER_HEIGHT = 70

# Постоянные игры
SHIFT = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
SEASONS = ((6, 5), (4, 5), (3, 5), (5, 5))
MOVE_DECREMENT = 1
START_ENERGY = 100
DIVISION_ENERGY = 500
MUTATION_CHANCE = 0.25

# Настройки отображения
SHOW_DIR = True
SHOW_ENERGY = True

# Шрифты
cube_font = pg.font.Font('fonts/mainFont.ttf', 16)
