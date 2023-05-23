import pygame as pg




class Stat():
    def __init__(self):
        self.reset_stat()
        # with open('record.txt') as f :
        #     self.record_score=int(f.readline())


    def reset_stat(self):
        self.score = 0
        self.live = 2

    def draw_life(self,screen,filename,x,y):
        self.x=x
        self.y=y
        for i in range(self.live+1):
            screen.blit(filename,(self.x,self.y))
            self.x-=50

