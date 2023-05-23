import pygame as pg
from sprite_ship import Ship
from random import randint

class Ball(pg.sprite.Sprite):
    '''солдаем класс Ball  '''
    def __init__(self,x, filename,speed,group,hp):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 11):
            img = pg.image.load(f'img/rotationY{num}.png')
            img = pg.transform.scale(img, (200, 200))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect=self.image.get_rect(center=(x,0))
        self.speed=speed
        self.add(group)
        self.hp =hp
        self.ship = Ship
        self.counter = 0
    def update(self,*args):
        explosion_speed = 4
        self.counter += 1
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        else:
            self.kill()

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.index =0

