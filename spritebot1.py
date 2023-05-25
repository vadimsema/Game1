import pygame as pg
from spriteBulletbot import Bulletsbot
from random import randint

class bot1(pg.sprite.Sprite):
    def __init__(self,x,filename,group,hp,speed,timebullet):
        pg.sprite.Sprite.__init__(self)
        self.x  = x
        self.image = pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(x,0))
        self.speed = speed
        self.add(group)
        self.counter_bullet=0
        self.counter = 0
        self.counter1 = 0
        self.timebullet =timebullet
        self.hp = hp
    def update(self,*args):
        if self.rect.y < args[0] - 900:
            self.rect.y += self.speed
        else:
            if self.counter1 < 300:
                self.rect.x -= 1
                self.counter1 += 1
            else:
                if 300 <= self.counter1 < 600:
                    self.rect.x += 1
                    self.counter1 += 1
                else:
                    self.counter1 = 0
            if self.counter_bullet ==self.timebullet :
                new_bulletbot = Bulletsbot(args[1], self, args[3])
                new_bulletbot.add(args[3])
                self.counter = 0
                self.counter_bullet = 0
            else:
                self.counter += 1
                self.counter_bullet += 1
















