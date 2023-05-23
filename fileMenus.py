import pygame as pg
import sys


bg=pg.image.load('img/pngwing.com.png')
class Game_menu():
    def __init__(self,punkts=[((100,100),'Start',(255,0,0),(0,0,255),0)]):
        self.punkts=punkts
    def drow_menu(self,screen,num_punkt):
        f = pg.font.SysFont('arial', 25, True)
        for i in self.punkts:
            if num_punkt == i[4]:
                img1=f.render(i[1],True,i[2])
                screen.blit(img1,i[0])
            else:
                img2 = f.render(i[1], True, i[3])
                screen.blit(img2, i[0])
    def choice_menu(self,screen,stat, menuSetting):
        num_punkt = 0
        menu_start = True






        while menu_start:

            mouse_pos =pg.mouse.get_pos()
            for punkt in self.punkts:
                if mouse_pos[0]>punkt[0][0] and mouse_pos[0]<punkt[0][0]+100 and \
                        mouse_pos[1] > punkt[0][1] and mouse_pos[1] < punkt[0][1] + 50:
                    num_punkt = punkt[4]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if num_punkt == 0:
                            menu_start = False
                        elif num_punkt==1:
                            stat.punkt_stat(screen)
                        elif num_punkt == 2:
                            menuSetting.choice_menuSET(screen, stat)
                        elif num_punkt == 3:
                            sys.exit()
                elif event.type  == pg.KEYDOWN:
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
                            stat.punkt_stat(screen)
                        elif num_punkt == 2:
                            menuSetting.choice_menuSET(screen, stat)
                        elif num_punkt == 3:
                            sys.exit()
            screen.blit(bg,(0,0))
            self.drow_menu(screen, num_punkt)
            pg.display.flip()



    def choice_menuSET(self, screen, stat):
        num_punkt = 0
        menu_start = True
        while menu_start:
            mouse_pos = pg.mouse.get_pos()
            for punkt in self.punkts:
                if mouse_pos[0] > punkt[0][0] and mouse_pos[0] < punkt[0][0] + 100 and \
                        mouse_pos[1] > punkt[0][1] and mouse_pos[1] < punkt[0][1] + 50:
                    num_punkt = punkt[4]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if num_punkt == 0:
                            stat.live=2
                        elif num_punkt == 1:
                            stat.live=1
                        elif num_punkt == 2:
                            stat.live=0
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if num_punkt > 0:
                            num_punkt -= 1
                    if event.key == pg.K_DOWN:
                        if num_punkt < len(self.punkts) - 1:
                            num_punkt += 1
                    if event.key == pg.K_RETURN:
                        if num_punkt == 0:
                            stat.live = 2
                        elif num_punkt == 1:
                            stat.live = 1
                        elif num_punkt == 2:
                            stat.live = 0
                    if event.key==pg.K_ESCAPE:
                        menu_start=False
            screen.blit(bg, (0, 0))
            self.drow_menu(screen, num_punkt)
            pg.display.flip()