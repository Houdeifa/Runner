import pygame
class Background:
    initalPos = (0,0)
    indexMove = 0
    indexBackground = 0
    movingSpeed = 10
    def __init__(self,screen,pos,scale=1):
        self.platfomImg = pygame.image.load('Jungle/PNG/jungle_pack_05.png')
        self.backgroundImg = pygame.image.load('Jungle/PNG/bg_jungle.png')
        size = self.platfomImg.get_size()
        self.platfomImg = pygame.transform.scale(self.platfomImg, (int(size[0]*scale), int(size[1]*scale)))
        size = self.backgroundImg.get_size()
        bgHeigth = pos[1]
        bgWidth = (pos[1]/size[1])*size[0]
        self.backgroundImg = pygame.transform.scale(self.backgroundImg, (int(bgWidth), int(bgHeigth)))
        self.screen = screen
        self.initalPos = pos

    def animate(self):
        w, h = self.screen.get_size()

        #background
        bgW, bgH = self.backgroundImg.get_size()
        self.screen.blit(self.backgroundImg,(0-self.indexBackground,0))
        self.screen.blit(self.backgroundImg,(bgW-self.indexBackground,0))
        self.indexBackground = (self.indexBackground + (self.movingSpeed/20)) % bgW
        
        #platform
        platW, platH = self.platfomImg.get_size()
        numbersOfImages = w/platW
        for i in range(int(numbersOfImages)+1):
            pos = (self.initalPos[0]+i*platW-self.indexMove,self.initalPos[1])
            self.screen.blit(self.platfomImg,pos)
            #pygame.draw.rect(self.screen,(255,255,255),(pos[0],pos[1],platW,platH))
        self.indexMove = (self.indexMove + self.movingSpeed) % platW
