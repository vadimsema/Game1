import pygame as pg
from sprite_bullet import Bullets

class Ship(pg.sprite.Sprite):
    '''солдаем класс Telega  '''

    def __init__(self,x,y, filename,speed ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))
        self.speed=speed



    def update(self,*args):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.x+10 >0 or keys[pg.K_LEFT] and self.rect.x+10 >0 or keys[pg.K_LEFT] and self.rect.x+10 >0:
            self.rect.x-=self.speed
        if keys[pg.K_d]  and self.rect.x+self.rect.width-15 < args[0] or keys[pg.K_RIGHT] and self.rect.x+self.rect.width-15 < args[0] :
            self.rect.x += self.speed
        if keys[pg.K_w]  and self.rect.y-6 >0 or keys[pg.K_UP] and self.rect.y-6 >0:
            self.rect.y-=self.speed
        if keys[pg.K_s]  and self.rect.y+self.rect.height-20 < args[1] or keys[pg.K_DOWN] and self.rect.y+self.rect.height-20 < args[1]:
            self.rect.y += self.speed


