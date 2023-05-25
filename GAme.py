import pygame as pg
from random import randint
from spriteball import Ball
from sprite_ship import Ship
from spriteBullet import Bullets
from statGame import Stat
from fileMenus import Game_menu
from spritebot1 import bot1
from spritebot2 import bot2
import sys
from sprite_bonus import Bonus


WIDTH=1800
HEUGHT=1000
FPS=60
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
pg.init()
s = pg.mixer.Sound('sound/blaster-2-81267.mp3')
bomm_sound =pg.mixer.Sound('sound/hq-explosion-6288.mp3')
pg.mixer.music.load('sound/227558-6ea81a03-cbc1-4d18-bdd6-9b031c6752ab.mp3')
pg.mixer.music.play(-1)

create_ball = pg.USEREVENT
create_bot1=pg.USEREVENT+1
create_bot2=pg.USEREVENT+2
next_lvl=pg.USEREVENT+3
pg.time.set_timer(create_ball,1500)
pg.time.set_timer(create_bot1,4000)
pg.time.set_timer(create_bot2,7000)
pg.time.set_timer(next_lvl,30000)

screen=pg.display.set_mode((WIDTH,HEUGHT))
pg.display.set_caption('my game')
clock=pg.time.Clock()
speed=15
image_life=pg.image.load('img/heart.png')
bg =pg.image.load('img/pngwing.com.png')
explosion_img = ['img/bubble_explo1.png','img/bubble_explo2.png','img/bubble_explo3.png','img/bubble_explo4.png','img/bubble_explo5.png'
                 'img/bubble_explo6.png','img/bubble_explo7.png','img/bubble_explo8.png','img/bubble_explo9.png','img/bubble_explo10.png']
stat_game = Stat()
punkts=[((WIDTH//2-100,HEUGHT//2-50),'Start',GREEN,BLUE,0),
((WIDTH//2-175,HEUGHT//2+150),'Statistic',GREEN,BLUE,2),
    ((WIDTH//2-100,HEUGHT//2+350),'Quit',GREEN,BLUE,1)]


menu=Game_menu(punkts)
menu.choice_menu(screen,stat_game)
ball_img=['img/rotationY2.png','img/rotationY3.png','img/rotationY4.png','img/rotationY5.png','img/rotationY2.png','img/rotationY6.png','img/rotationY7.png']
ship = Ship(WIDTH//2, HEUGHT-135, 'img/Transforming fighter ship 1_000.png',speed)


bullet_img='img/blasterbolt.png'
bulletred_img='img/blasterboltred.png'
f = pg.font.SysFont('arial',25,True)
f1 = pg.font.SysFont('arial',75,True)
stat_game = Stat()
start = True
restar= True
game_score = 0
widsboom= 150
hightbomm = 150
def restart_game():
    global restar,ship,bgkard
    text_p = f.render('To restart the game click R', True, (0, 255, 0))
    text_p1 = f.render('To exit the game click Q', True, (0, 255, 0))
    text_p2 = f1.render('YOU LOSE', True, (255, 0, 0))
    screen.blit(text_p, (WIDTH // 2-120, HEUGHT // 2-50))
    screen.blit(text_p1, (WIDTH // 2 - 120, HEUGHT // 2 ))
    screen.blit(text_p2,(WIDTH // 2 - 150,HEUGHT//2-150))
    restar = True
    while restar:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    sys.exit()
                elif event.key == pg.K_r:
                    restar = False
                    balls.empty()
                    ship = Ship(WIDTH // 2, HEUGHT - 135, 'img/Transforming fighter ship 1_000.png', speed)
                    stat_game.live=2
                    bgkard = -1700
                    explosion_group.empty()
                    bots1.empty()
                    bullets_gr1.empty()
                    bullets_gr.empty()
                    bots2.empty()
                    pg.mixer.music.rewind()
        pg.display.flip()
        clock.tick(FPS)




def creatball(group):
    x=randint(100,WIDTH-100)
    speed = stat_game.speedball
    return Ball(x,ball_img[randint(0,6)] , speed, group,2)

def collid():
    global game_score,bonus_gr
    for bullet in bullets_gr:
        for ball in balls:
            if ball.rect.collidepoint(bullet.rect.centerx,bullet.rect.centery):
                if ball.hp >0:
                    ball.hp-=1
                    bullet.kill()
                    new_boom = Explosion(bullet.rect.centerx, bullet.rect.centery, 75, 75)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                else:
                    new_boom = Explosion(ball.rect.centerx, ball.rect.centery,300,300)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                    ball.kill()
                    bullet.kill()

    for bot2 in bots2:
        if bot2.rect.collidepoint(ship.rect.centerx,ship.rect.centery):
            new_boom = Explosion(bot2.rect.centerx, bot2.rect.centery, 250, 250)
            explosion_group.add(new_boom)
            bot2.kill()
            if stat_game.live > 0:
                stat_game.live -= 1
                bomm_sound.play()
            else:
                restart_game()
                bomm_sound.play()

    for bullet in bullets_gr:
        for bot1 in bots1:
            if bot1.rect.collidepoint(bullet.rect.centerx,bullet.rect.centery):
                if bot1.hp >0:
                    bot1.hp-=1
                    bullet.kill()
                    new_boom = Explosion(bot1.rect.centerx, bot1.rect.centery, 75, 75)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                else:
                    new_boom = Explosion(bot1.rect.centerx, bot1.rect.centery,200,200)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                    new_bonus=Bonus(bot1.rect.centerx,bot1.rect.centery,'img/heart.png',0,bonus_gr)
                    stat_game.score+=100

                    bot1.kill()
                    bullet.kill()

        for bot2 in bots2:
            if bot2.rect.collidepoint(bullet.rect.centerx,bullet.rect.centery):
                if bot2.hp >0:
                    bot2.hp-=1
                    bullet.kill()
                    new_boom = Explosion(bot2.rect.centerx, bot2.rect.centery, 75, 75)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                else:
                    new_boom = Explosion(bot2.rect.centerx, bot2.rect.centery,200,200)
                    explosion_group.add(new_boom)
                    bomm_sound.play()
                    stat_game.score += 200
                    bot2.kill()
                    bullet.kill()

    for bullet in bullets_gr1:
        if ship.rect.collidepoint(bullet.rect.centerx, bullet.rect.centery):
            bullet.kill()
            new_boom = Explosion(ship.rect.centerx, ship.rect.centery, 150, 150)
            explosion_group.add(new_boom)
            bomm_sound.play()
            if stat_game.live > 0:
                stat_game.live -= 1
            else:
                restart_game()
    for ball in balls:
        if ball.rect.collidepoint(ship.rect.centerx,ship.rect.centery):
            ball.kill()
            new_boom = Explosion(ship.rect.centerx, ship.rect.centery,150,150)
            explosion_group.add(new_boom)
            bomm_sound.play()
            if stat_game.live>0:
                stat_game.live-=1
            else:
                restart_game()


def check_record():
    if stat_game.score>stat_game.record_score:
        stat_game.record_score=stat_game.score
    with open('Statistic.txt', 'w') as f:
        f.write(str(stat_game.record_score))
        f.write('\n')
        f.write(str(stat_game.in_game))

def unpause():
    global pause
    pause= False
def paused():
    f5 = pg.font.SysFont('arial', 75, True)
    text_p = f5.render('PAUSE',True,(0,255,0))
    screen.blit(text_p,(WIDTH//2-100,HEUGHT//2-75))
    while pause:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    unpause()
        pg.display.flip()
        clock.tick(FPS)



class Explosion(pg.sprite.Sprite):
    def __init__(self,x,y,width,hight):
        pg.sprite.Sprite.__init__(self)
        self.images =[]
        self.widthboom = width
        self.hightboom = hight
        for num in range(1,11):
            img = pg. image.load(f'img/bubble_explo{num}.png')
            img= pg.transform.scale(img,(self.widthboom,self.hightboom))
            self.images.append(img)
        self.index = 0
        self.image= self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
    def update(self):
        explosion_speed = 4
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index +=1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter>=explosion_speed:
            self.kill()

explosion_group =pg.sprite.Group()






balls=pg.sprite.Group()
creatball(balls)
bullets_gr = pg.sprite.Group()
bonus_gr = pg.sprite.Group()
bgkard=-1700
bots1=pg.sprite.Group()
bots2=pg.sprite.Group()
bullets_gr1=pg.sprite.Group()
counter = 0
counter2 = 0

while start:
    events = pg.event.get()
    keys = pg.key.get_pressed()
    for event in events:
        if event.type==pg.QUIT or keys[pg.K_LALT] and keys[pg.K_F4]:
            start=False

        elif event.type == create_ball:
            creatball(balls)
        elif event.type == create_bot1:
            new_bot = bot1(randint(300, WIDTH-300),'img/5cyRAIO.png' , bots1,1,stat_game.speedbot1,stat_game.timebullet)
        elif event.type == create_bot2:
            new_bot2 = bot2(randint(700, WIDTH - 700), 'img/fighter.png', bots2, 3,stat_game.speedbot2)
        elif event.type == next_lvl:
            stat_game.speedbot1 += 1
            stat_game.timebullet -= 5
            stat_game.speedbot2 += 1
            stat_game.speedball += 1

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                new_bullet = Bullets(bullet_img, ship, bullets_gr)
                new_bullet.add(bullets_gr)
                s.play()
            elif event.key == pg.K_ESCAPE:
                pause = True
                paused()

    if bgkard==0:
        bgkard  -=1700
    else:
        bgkard += 1

    print(len(bonus_gr))



    screen.blit(bg, (0, bgkard))
    bonus_gr.update()
    bonus_gr.draw(screen)
    bots1.draw(screen)
    bots1.update(HEUGHT, bulletred_img, ship, bullets_gr1)
    bots2.draw(screen)
    bots2.update(HEUGHT,ship.rect.centerx)
    balls.draw(screen)
    balls.update(HEUGHT)
    collid()
    screen.blit(ship.image, ship.rect)
    ship.update(WIDTH, HEUGHT)
    explosion_group.draw(screen)
    explosion_group.update()
    bullets_gr.draw(screen)
    bullets_gr.update()
    bullets_gr1.draw(screen)
    bullets_gr1.update(HEUGHT)
    stat_game.draw_life(screen, image_life, 1650, 100)
    check_record()
    score_f = f1.render(str(stat_game.score), True, GREEN)
    screen.blit(score_f, (WIDTH//2-20, 50))
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
#hgfalusbvibspivbpiBPVIwrpihvpiuWHVPIUBPIYGPwiuhfv