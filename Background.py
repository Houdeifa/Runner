import pygame
class Background:
    initalPos = (0,0)
    indexMove = 0
    indexBackground = 0
    movingSpeed = 10
    def __init__(self,screen,pos,scale=1):
        self.loadImages()
        self.platfomImg = self.reScale(self.platfomImg,scale)
        size = self.backgroundImg.get_size()
        self.backgroundImg = self.reScaleWH(self.backgroundImg,(pos[1]/size[1])*size[0],pos[1])
        self.screen = screen
        self.initalPos = pos

    def loadImages(self):
        self.platfomImg = pygame.image.load('Jungle/PNG/jungle_pack_05.png')
        self.backgroundImg = pygame.image.load('Jungle/PNG/bg_jungle.png')

    def animateBackground(self):
        #background
        bgW, bgH = self.backgroundImg.get_size()
        self.screen.blit(self.backgroundImg,(0-self.indexBackground,0))
        self.screen.blit(self.backgroundImg,(bgW-self.indexBackground,0))
        self.indexBackground = (self.indexBackground + (self.movingSpeed/20)) % bgW

    def animatePlatform(self):
        #platform
        w, h = self.screen.get_size()
        platW, platH = self.platfomImg.get_size()
        numbersOfImages = w/platW
        for i in range(int(numbersOfImages)+1):
            pos = (self.initalPos[0]+i*platW-self.indexMove,self.initalPos[1])
            self.screen.blit(self.platfomImg,pos)
        self.indexMove = (self.indexMove + self.movingSpeed) % platW

    def animate(self):
        self.animateBackground()
        self.animatePlatform()
    
    def reScale(self,img,scale):
        size = img.get_size()
        return pygame.transform.scale(img, (int(size[0]*scale), int(size[1]*scale)))
    def reScaleWH(self,img,width,height):
        return pygame.transform.scale(img, (int(width), int(height)))
        
