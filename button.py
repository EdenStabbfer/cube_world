import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, image=None, text=None):
        super().__init__()
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.text = text

    def blit_me(self):
        self.surface.blit(self.image, (self.x, self.y))
