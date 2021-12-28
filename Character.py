import pygame
from Ressources import Ressources

class Character:
    res = Ressources(0.2)
    runIndex = 0
    jumpIndex = 0
    runSpeed = 0.4
    jumpSpeed = 0.2
    initalPos = (0,0)
    size = res.RunImgs[0].get_size()
    jumpRange = 100
    hitBox = (initalPos[0],initalPos[1],size[0],size[1])
    etat = 0 # 0 ==> running , 1 ==> jumping
    pos = ()

    def __init__(self,screen,initalPos=(0,0),jumpRange=100):
        self.screen = screen
        self.initalPos = (initalPos[0], initalPos[1]-self.size[1]) 
        self.jumpRange = jumpRange
    def animate(self):
        if(self.etat == 0):
            self.runAnimation()
        elif(self.etat == 1):
            self.jumpAnimation()
        self.hitBox = (self.pos[0]+(50/193)*self.size[0],self.pos[1]+(22/193)*self.size[1],self.size[0]*80/193,self.size[1]*134/160)
        self.drawHitBox()
    def runAnimation(self):
        self.pos = self.initalPos
        self.screen.blit(self.res.RunImgs[int(self.runIndex)],self.initalPos)
        self.runIndex = (self.runIndex + self.runSpeed) % 7
    def jumpAnimation(self):        
        jumpDistance2 = self.jumpIndex/5 - 1
        jumpDistance2 *= jumpDistance2
        jumpDistance2 *= self.jumpRange
        jumpDistance2 = self.jumpRange - jumpDistance2
        self.pos =  (self.initalPos[0],self.initalPos[1] - jumpDistance2)

        self.screen.blit(self.res.JumpImgs[int(self.jumpIndex)],self.pos)
        self.jumpIndex+=self.jumpSpeed
        if(self.jumpIndex > 10):
            self.jumpIndex = 0
            self.etat = 0
    def jump(self):
        if(self.etat == 0):
            self.etat = 1
            self.runIndex = 0
    def drawHitBox(self):
        pygame.draw.rect(self.screen,(255,255,255),self.hitBox,2)

    def didHit(self,obj,i):
        # 0 : x , 1 : y , 2 : w , 3 : h
        #right : x+w , left : x, top : y, bottom : y+h

        #if rectB.right < rectA.left:
        if obj.right(i) < self.left():
            return False
        #if rectB.bottom < rectA.top:
        if obj.bottom(i) < self.top():
            return False
        #if rectB.left > rectA.right:
        if obj.left(i)> self.right():
            return False
        #if rectB.top > rectA.bottom:
        if obj.top(i) > self.bottom():
            return False
        return True

    def right(self):
        return self.hitBox[0]+self.hitBox[2]
    def left(self):
        return self.hitBox[0]
    def top(self):
        return self.hitBox[1]
    def bottom(self):
        return self.hitBox[1]+self.hitBox[3]