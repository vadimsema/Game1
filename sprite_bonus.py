import pygame as pg
class Bonus(pg.sprite.Sprite):
    def __init__(self,x,y,filename,bonus,group):
        pg.sprite.Sprite.__init__(self)
        self.x =x
        self.y=y
        self.image=pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.bonus = bonus
        self.speed=5
        self.add(group)
    def update(self):
        if self.rect.y > 0:
            self.rect.y += self.speed
        else:
            self.kill()



