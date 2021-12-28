import pygame
class Objects:
    timeIndex = 0
    cactusArray = []
    cactSpeed = 3
    hitBox = []
    def __init__(self,screen,initalPos,scale=1):
        self.cactusImg = pygame.image.load('deserttileset\png\Objects\Cactus (1).png')
        size = self.cactusImg.get_size()
        self.cactusImg = pygame.transform.scale(self.cactusImg, (int(size[0]*scale), int(size[1]*scale)))
        self.screen = screen
        self.cactusSize = self.cactusImg.get_size()
        self.initalPos = (initalPos[0],initalPos[1]-self.cactusSize[1])
        
    def animate(self):
        self.timeIndex += self.cactSpeed
        if(self.timeIndex > 200):
            self.timeIndex = 0
            self.cactusArray.append(self.initalPos)
            self.hitBox.append((self.initalPos[0],self.initalPos[1],self.cactusSize[0],self.cactusSize[1]))
        for i in range(len(self.cactusArray)):
            self.screen.blit(self.cactusImg,self.cactusArray[i])
            self.cactusArray[i] = (self.cactusArray[i][0]-self.cactSpeed,self.cactusArray[i][1])
            self.hitBox[i] = (self.cactusArray[i][0],self.cactusArray[i][1],self.cactusSize[0],self.cactusSize[1])
            pygame.draw.rect(self.screen,(255,255,255),self.hitBox[i],2)

    def right(self,i):
        return self.hitBox[i][0]+self.hitBox[i][2]
    def left(self,i):
        return self.hitBox[i][0]
    def top(self,i):
        return self.hitBox[i][1]
    def bottom(self,i):
        return self.hitBox[i][1]+self.hitBox[i][3]

    def didHit(self,charct):
        for i in range(len(self.hitBox)):
            if(charct.didHit(self,i)):
                return True
        return False