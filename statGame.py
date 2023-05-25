import pygame as pg




class Stat():
    def __init__(self):
        self.reset_stat()
        with open('Statistic.txt') as f :
            self.record_score=int(f.readline())
            self.in_game = int(f.readline())



    def reset_stat(self):
        self.score = 0
        self.live = 2
        self.speedbot1 = 5
        self.timebullet =50
        self.speedbot2=10
        self.speedball = 7

    def draw_life(self,screen,filename,x,y):
        self.x=x
        self.y=y
        for i in range(self.live+1):
            screen.blit(filename,(self.x,self.y))
            self.x-=50

