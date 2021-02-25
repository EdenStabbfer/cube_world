import pygame as pg
from random import randint, random

from bot.cube import Cube
from bot.corpse import Corpse
from settings import SHIFT, MOVE_DECREMENT, SHOW_DIR, START_ENERGY, LINE_WIDTH, SHOW_ENERGY, MUTATION_CHANCE, cube_font
from enums import ObjectId


class Bot(Cube):
    def __init__(self, surface, group, size, cords, genom):
        super().__init__(surface, size, cords)
        self.group = group
        self.genom = genom

        self.colour = (85, 230, 15)
        self.id = 0
        self.type = ObjectId.BOT
        self.pointer = 0
        self.dir = randint(0, 7)
        self.energy = START_ENERGY
        self.life = 0

    # Обновление координат и позиции бота
    def move(self):
        if not self.is_anyone_in_front():
            self.wx += SHIFT[self.dir][0]
            self.wy += SHIFT[self.dir][1]
            self.x = self.wx * (self.size + LINE_WIDTH)
            self.y = self.wy * (self.size + LINE_WIDTH)
            self.energy -= MOVE_DECREMENT

    # Деление клетки
    def division(self):
        cords = self.is_anyone_around()
        if cords:
            baby = Bot(self.surface, self.group, self.size, cords, self.genom)
            baby.mutation()
            self.group.add(baby)
            self.energy = START_ENERGY

    def eat(self):
        in_front_obj = self.is_anyone_in_front()
        if in_front_obj and self in self.group and \
                (in_front_obj.type is ObjectId.BOT or in_front_obj.type is ObjectId.CORPSE):
            self.energy += in_front_obj.energy
            self.group.remove(in_front_obj)

    def attack(self):
        pass

    def mutation(self):
        chance = randint(0, 3)
        if chance == 0:
            self.genom[randint(0, 31)] = randint(0, 31)

    # Возврацает объект впереди, если тот присутствует
    def is_anyone_in_front(self):
        new_wx, new_wy = self.wx + SHIFT[self.dir][0], self.wy + SHIFT[self.dir][1]
        for bot in self.group.copy():
            if bot.get_w_cords() == (new_wx, new_wy):
                return bot
        return False

    # Если никого вокруг, то возврацаем координаты
    def is_anyone_around(self):
        for i in range(8):
            new_wx = self.wx + SHIFT[(self.dir + i + 4) % 8][0]
            new_wy = self.wy + SHIFT[(self.dir + i + 4) % 8][1]
            find = False
            for cube in self.group.copy():
                if (new_wx, new_wy) == cube.get_w_cords():
                    find = True
            # Если никого впереди, то возврацаем координаты
            if not find:
                return new_wx, new_wy
        return False

    # Отрисовка бота
    def draw_me(self):
        pg.draw.rect(
            self.surface,
            self.colour,
            pg.Rect(self.x, self.y, self.size, self.size))
        if SHOW_DIR:
            pg.draw.line(self.surface, (0, 0, 0), (self.x+self.size//2, self.y+self.size//2),
                     (self.x+(SHIFT[self.dir][0]+1)*self.size//2, self.y+(SHIFT[self.dir][1]+1)*self.size//2), 2)
        if SHOW_ENERGY:
            text = cube_font.render(str(self.energy), False, (0, 0, 0))
            x_offset = (self.size - text.get_width()) // 2
            y_offset = (self.size - text.get_height()) // 2
            self.surface.blit(text, (self.x + x_offset, self.y + y_offset))

    # Получить команду по гену
    def get_command(self, shift=0):
        return self.genom[self.pointer + shift]

    # Безусловный переход по геному
    def set_command(self, shift):
        self.pointer = (self.pointer + self.genom[(self.pointer + shift) % 32]) % 32
