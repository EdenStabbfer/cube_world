from bot import Wall, Bot, Corpse
from settings import SEASONS, CUBE_SIZE, START_ENERGY, DIVISION_ENERGY
from enums import Command, ObjectId
from pickle import dump


def draw_walls(surface, cubes, world_width, world_height, size):
    for i in range(world_width):
        wall1 = Wall(surface, size, (i, 0))
        wall2 = Wall(surface, size, (i, world_height-1))
        cubes.add(wall1)
        cubes.add(wall2)
        wall1.draw_me()
        wall2.draw_me()

    for j in range(1, world_height-1):
        wall1 = Wall(surface, size, (0, j))
        wall2 = Wall(surface, size, (world_width-1, j))
        cubes.add(wall1)
        cubes.add(wall2)
        wall1.draw_me()
        wall2.draw_me()


def photosynthesis(wy, incr, season):
    level = wy // incr
    if level < SEASONS[season][0]:
        return SEASONS[season][0] - level
    else:
        return 0


def chemosynthesis(wy, world_height, incr, season):
    level = (world_height - wy) // incr - 1
    if level <= SEASONS[season][1]:
        return SEASONS[season][1] - level
    else:
        return 0


def cell_updater(group, game_surf, world_height, season_incr, cur_season):
    # Если бот зависает у стенки, значит не может выполнить команду после ПОСМОТРЕТЬ
    for obj in group.copy():
        if obj.type is ObjectId.BOT:
            if obj.life > 1000:
                group.add(Corpse(game_surf, CUBE_SIZE, obj.get_w_cords(), START_ENERGY))
                group.remove(obj)
                continue
            elif obj.energy > DIVISION_ENERGY:
                obj.division()

            command = obj.get_command()
            if command == Command.ROTATE:
                obj.dir = (obj.dir + obj.get_command(1) % 8) % 8
                obj.set_command(2)
            elif command == Command.MOVE:
                obj.move()
                obj.set_command(1)
            elif command == Command.EAT:
                obj.eat()
                obj.set_command(1)
            elif command == Command.LOOKFORWARD:
                in_front_obj = obj.is_anyone_in_front()
                if in_front_obj:
                    type = in_front_obj.type
                    if type is ObjectId.WALL:
                        obj.set_command(2)
                    elif type is ObjectId.BOT:
                        obj.set_command(4)
                    elif type is ObjectId.CORPSE:
                        obj.set_command(3)
                else:
                    obj.set_command(1)
            elif command == Command.PHOTOSYNTHESIS:
                obj.energy += photosynthesis(obj.wy, season_incr, cur_season)
                obj.set_command(1)
            elif command == Command.CHEMOSYNTHESIS:
                obj.energy += chemosynthesis(obj.wy, world_height, season_incr, cur_season)
                obj.set_command(1)
            elif command == Command.MYENERGY:
                if obj.energy > obj.get_command(1)*30:
                    obj.set_command(2)
                else:
                    obj.set_command(3)
            elif command == Command.ATTACK:
                obj.attack()
            else:  # Безусловный переход
                obj.set_command(command)
            obj.life += 1



# Сохранение данных игры:
def save_game(group):
    file = open("data/game_data.dat", "bw")
    txt_file = open("data/game_data.txt", "w")
    for obj in group:
        if hasattr(obj, "genom"):
            dump(obj.genom, file)
            txt_file.write(str(obj.genom)+"\n")
    file.close()
