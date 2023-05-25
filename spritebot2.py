import pygame as pg
from spriteBulletbot import Bulletsbot




class bot2(pg.sprite.Sprite):
    def __init__(self,x,filename,group,hp,speed):
        pg.sprite.Sprite.__init__(self)
        self.x  = x
        self.image = pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(x,0))
        self.speed = speed
        self.speedrun = 8
        self.add(group)
        self.counter = 0
        self.counter1 = 0
        self.hp = hp
    def update(self,*args):
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        elif self.rect.y >args[0]-500:
            self.speed = 10
        else:
            self.kill()
        if self.rect.x >args[1]-30:
            self.rect.x -=self.speedrun
        if self.rect.x <args[1]-30:
            self.rect.x +=self.speedrun

