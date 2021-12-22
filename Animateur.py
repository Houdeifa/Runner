import pygame
from Ressources import Ressources


class Animateur:
    RunIndex = 0
    JumpIndex = 0
    speed = 0.4
    jumpSpeed = 0.4
    state = 'R'
    res = Ressources(0.2)
    def __init__(self,screen,speed=0.4):
        self.screen = screen
        self.speed = speed
    def runInc(self):
        self.RunIndex += self.speed
        if(self.RunIndex > 7):
            self.RunIndex = 0
    def jumpInc(self):
        self.JumpIndex += self.jumpSpeed
        if(self.JumpIndex > 9):
            self.JumpIndex = 0
            self.state = 'R'
    def Animate(self):
        if(self.state == 'R'):
            self.screen.blit(self.res.RunImgs[int(self.RunIndex)], (0,0))
            self.runInc()
        elif(self.state == 'J'):
            self.screen.blit(self.res.JumpImgs[int(self.JumpIndex)], (0,0))
            self.jumpInc()
    def Jump(self):
        self.state = 'J'
        self.RunIndex = 0
        self.JumpIndex = 0

