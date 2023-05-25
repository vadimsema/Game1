import pygame as pg
from statGame import Stat
import sys
WIDTH=1800
HEUGHT=1000
Green=(0,255,0)
bg=pg.image.load('img/pngwing.com.png')
Button = pg.image.load('img/ButtonStock1h.png')
galaga = pg.image.load('img/galaga.png')
Statictic=True
stat_game =Stat()
class Game_menu():
    def __init__(self,punkts=[((100,100),'Start',(255,0,0),(0,0,255),0)]):
        self.punkts=punkts
        self.bgkard=0
    def drow_menu(self,screen,num_punkt):
        f = pg.font.SysFont('arial', 100, True)
        for i in self.punkts:
            if num_punkt == i[4]:
                img1=f.render(i[1],True,i[2])
                screen.blit(img1,i[0])
            else:
                img2 = f.render(i[1], True, i[3])
                screen.blit(img2, i[0])
    def choice_menu(self,screen,stat):
        num_punkt = 0
        menu_start = True
        f = pg.font.SysFont('arial', 130, True)
        f1 =pg.font.SysFont('arial', 90, True)
        f2 = pg.font.SysFont('arial', 60, True)
        total_attempts=f1.render('Attempts',True,(216,166,0))
        record_int = f2.render(str(stat_game.record_score), True, (194,149,0))
        in_game_int = f2.render(str(stat_game.in_game), True, (194,149,0))
        Statit = f.render('Statistics', True, (233,179,0))
        Record = f1.render('Record', True, (216,166,0))

        while menu_start:
            keys = pg.key.get_pressed()
            mouse_pos =pg.mouse.get_pos()
            for punkt in self.punkts:
                if mouse_pos[0]>punkt[0][0] and mouse_pos[0]<punkt[0][0]+200 and \
                        mouse_pos[1] > punkt[0][1] and mouse_pos[1] < punkt[0][1] +100:
                    num_punkt = punkt[4]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if num_punkt == 0:
                            menu_start = False
                            with open('Statistic.txt', 'w') as f:
                                f.write(str(stat_game.record_score))
                                f.write('\n')
                                f.write(str(stat_game.in_game+1))
                        elif num_punkt == 1:
                            sys.exit()


                        elif num_punkt == 2:
                            while Statictic:
                                keys = pg.key.get_pressed()
                                for event in pg.event.get():
                                    if event.type == pg.QUIT or keys[pg.K_LALT] and keys[pg.K_F4]:
                                        sys.exit()
                                    elif event.type == pg.KEYDOWN:
                                        if event.key == pg.K_ESCAPE:
                                            Statictic=False
                                if self.bgkard <= -1700:
                                    self.bgkard = 0
                                else:
                                    self.bgkard -= 0.1
                                screen.blit(bg, (0, self.bgkard))
                                pg.draw.rect(screen,(51,67,166),pg.Rect(750,185,370,140))
                                pg.draw.rect(screen, (51, 67, 166), pg.Rect(730, 430, 425, 150))
                                screen.blit(Statit, (WIDTH//2-220, 30))
                                screen.blit(Record, (WIDTH // 2 - 120, 200))
                                screen.blit(record_int, (WIDTH // 2 -30, 350))
                                screen.blit(total_attempts, (WIDTH // 2 - 150, 450))
                                screen.blit(in_game_int, (WIDTH // 2 , 600))
                                pg.display.flip()


                elif event.type  == pg.KEYDOWN:
                    if event.type == pg.QUIT or keys[pg.K_LALT] and keys[pg.K_F4]:
                        sys.exit()
                    if event.key == pg.K_UP:
                        if num_punkt>0:
                            num_punkt -=1
                    if event.key == pg.K_DOWN:
                        if num_punkt<len(self.punkts)-1:
                            num_punkt+=1
                    if event.key == pg.K_RETURN:
                        if num_punkt == 0:
                            menu_start = False
                        elif num_punkt == 1:
                            sys.exit()
                        elif num_punkt == 2:
                            while Statictic:
                                for event in pg.event.get():
                                    if event.type == pg.QUIT:
                                        sys.exit()
                                    elif event.type == pg.KEYDOWN:
                                        if event.key == pg.K_ESCAPE:
                                            Statictic=False
                                if self.bgkard <= -1700:
                                    self.bgkard = 0
                                else:
                                    self.bgkard -= 0.1
                                screen.blit(bg, (0, self.bgkard))
                                pg.display.flip()
            Statictic=True
            if self.bgkard <= -1700:
                self.bgkard = 0
            else:
                self.bgkard -= 1
            screen.blit(bg,(0,self.bgkard))
            screen.blit(Button,((WIDTH//2-210,HEUGHT//2-135)))
            screen.blit(Button, ((WIDTH // 2 - 210, HEUGHT // 2 +65)))
            screen.blit(Button, ((WIDTH // 2 - 210, HEUGHT // 2 + 265)))
            screen.blit(galaga,(WIDTH//2-300,50))
            self.drow_menu(screen, num_punkt)
            pg.display.flip()



