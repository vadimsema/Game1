import pygame as pg


class Bulletsbot(pg.sprite.Sprite):
    def __init__(self, filename, ship, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = 10
        self.add(group)
    def update(self,*args):
        if self.rect.y<args[0]:
            self.rect.y += self.speed
        else:
            self.kill()