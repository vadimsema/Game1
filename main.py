import pygame as pg
from random import randint
from spriteball import Ball
from sprite_ship import Ship
from spriteBullet import Bullets
WIDTH=1800
HEUGHT=1000
FPS=60
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
pg.init()
pg.time.set_timer(pg.USEREVENT,2000)
screen=pg.display.set_mode((WIDTH,HEUGHT))
pg.display.set_caption('my game')
clock=pg.time.Clock()
speed=15
bg =pg.image.load('img/nightskycolor.png')
ball_img=['img/rotationY2.png','img/rotationY3.png','img/rotationY4.png','img/rotationY5.png','img/rotationY2.png','img/rotationY6.png','img/rotationY7.png',]
ship = Ship(WIDTH//2, HEUGHT-135, 'img/Transforming fighter ship 1_061.png',speed)
bullet_img='img/blasterbolt.png'

start = True
def creatball(group):
    x=randint(30,WIDTH-30)
    speed = randint(5, 10)
    return Ball(x,ball_img[randint(0,6)] , speed, group)
balls=pg.sprite.Group()
creatball(balls)
bullets_gr = pg.sprite.Group()

while start:
    events = pg.event.get()
    for event in events:
        if event.type==pg.QUIT:
            start=False
        elif event.type == pg.USEREVENT:
            creatball(balls)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                new_bullet = Bullets(bullet_img, ship, bullets_gr)
                new_bullet.add(bullets_gr)
    screen.blit(bg, (0, 0))
    balls.draw(screen)
    balls.update(HEUGHT)
    screen.blit(ship.image, ship.rect)
    ship.update(WIDTH, HEUGHT)
    bullets_gr.draw(screen)
    bullets_gr.update()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
