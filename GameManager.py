from Background import Background
from Character import Character
from Objects import Objects
from Window import Window
import sys
import pygame

class GameManager:
    def __init__(self,screen):
        self.screen = screen
        self.etat = 0 # 0 => initial window, 1 => gaming , 2 => gameOver
        width, height = self.screen.get_size()
        hpos = height*2.6/3
        self.charact = Character(screen,(0,hpos),height/3)
        self.back = Background(screen,(0,hpos),0.5)
        self.obj = Objects(screen,(width,hpos),0.5)

        #start menu
        self.StartWin = Window(screen)
        self.StartWin.addButton("Continue",3,self.continueFunc)
        self.StartWin.addButton("New Game",0,self.newGameFunc)
        self.StartWin.addButton("Quit",0,self.quitFunc)
        self.StartWin.yPosCalc()


    def animate(self):
        if self.etat == 0:
            self.StartWin.animate()
        elif self.etat == 1:
            self.back.animate()
            self.charact.animate()
            self.obj.animate()
    
    def MouseClick(self):
        for i in range(len(self.StartWin.buttonsBoxes)):
            if(self.StartWin.isMouseIn(pygame.mouse.get_pos(),i)):
                self.StartWin.buttonsCallbacks[i]()
                break
    def continueFunc(self):
        pass
    def newGameFunc(self):
        self.etat = 1
    def quitFunc(self):
        pygame.quit()
        sys.exit()
    def checkLoose(self):
        if(self.obj.didHit(self.charact)):
             print("dead")