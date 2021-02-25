from enum import Enum


class Command(Enum):
    ROTATE = 20  # Поворот
    MOVE = 21  # Двигаться
    EAT = 22  # Съесть
    LOOKFORWARD = 23  # Посмотреть вперёд
    PHOTOSYNTHESIS = 24  # Фотосинтез
    CHEMOSYNTHESIS = 25  # Хемосинтез
    MYENERGY = 26
    ATTACK = 27
    LOOKAROUND = 28

    def __eq__(self, other):
        return self.value == other


class ObjectId(Enum):
    CUBE = 0  # Базовый класс (каркас)
    BOT = 1  # Бот
    WALL = 2  # Преграда
    CORPSE = 3  # Трупик

