from Background import Background
from Character import Character
from Objects import Objects
from Window import Window

class GameManager:
    def __init__(self,screen):
        self.screen = screen
        self.etat = 0 # 0 => initial window, 1 => gaming , 2 => gameOver
        width, height = self.screen.get_size()
        hpos = height*2.6/3
        self.charact = Character(screen,(0,hpos),height/3)
        self.back = Background(screen,(0,hpos),0.5)
        self.obj = Objects(screen,(width,hpos),0.5)
        self.win = Window(screen)

    def animate(self):
        if self.etat == 0:
            self.win.animate()
        elif self.etat == 1:
            self.back.animate()
            self.charact.animate()
            self.obj.animate()
