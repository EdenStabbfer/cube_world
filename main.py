import pygame as pg
from pygame.time import Clock
from random import randint

from grid import Grid
from functions import *
from settings import *
from button import Button


pg.init()
pg.display.set_caption("Cube World")

clock = Clock()
pg.time.set_timer(pg.USEREVENT, 125)


# Инициализация игровой сетки
grid = Grid(WIDTH, HEIGHT - HEADER_HEIGHT - FOOTER_HEIGHT, LINE_WIDTH, CUBE_SIZE, (95, 100, 105))
world_width, world_height = grid.get_world_size()
print(grid.get_adj_size())

# Поверхности
screen = pg.display.set_mode((WIDTH, HEIGHT))
header = pg.Surface((WIDTH, HEADER_HEIGHT))
header.fill((35, 45, 57))
footer = pg.Surface((WIDTH, FOOTER_HEIGHT))
footer.fill((35, 45, 57))
game_surf = pg.Surface((WIDTH, HEIGHT - HEADER_HEIGHT - FOOTER_HEIGHT))
grid_surf = grid.lines_generate()

# Инициализация кубиков
# [23, 6, 9, 12, 12, 18, 21, 0, 14, 20, randint(0, 6), 11, 22, 8] + [randint(0, 63) for i in range(50)]
cubes = pg.sprite.Group()
for i in range(1):
    genom = [23, 6, 14, 14, 14, 0, 26, 13, 4, 6, 21, 22, 24, 20, 20, 1, 18] + [randint(0, 31) for j in range(15)]
    cube = Bot(game_surf, cubes, CUBE_SIZE, (10, 4), genom)
    cube.id = i
    cubes.add(cube)


# Нарисовать стены
draw_walls(grid_surf, cubes, world_width, world_height, CUBE_SIZE)

# Сезоны
world_life = 0
season_duration = 1200  # t / 8 секунт
season_incr = world_height // 10

# TODO: Сделать изменение цвета при наведении
start_im = pg.transform.scale(pg.image.load("images/start.png").convert_alpha(), (50, 50))
start_button = Button(header, 5, 5, 50, 50, image=start_im)


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            save_game(cubes)
            pg.quit()
            quit()
        if e.type == pg.USEREVENT:
            # Обновление ботов
            cell_updater(cubes, game_surf, world_height, season_incr, (world_life // season_duration) % 4)
            world_life += 1

    # Отрисовка поверхностей
    start_button.blit_me()

    screen.blit(header, (0, 0))
    game_surf.blit(grid_surf, (0, 0))
    for bot in cubes:
        bot.draw_me()
    screen.blit(game_surf, (0, HEADER_HEIGHT))
    screen.blit(footer, (0, HEIGHT - FOOTER_HEIGHT))

    pg.display.update()
    clock.tick(30)
