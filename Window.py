import pygame
class Window:
    intialPos = ()
    defaultSize = ()
    defaultMargin = 0
    buttonsBoxes = [] # (x,y,w,h)
    buttonsTextes = [] # (x,y,w,h)
    buttonsStates = [] # 0 => normal, 1=> hoverd
    buttonCounter = 0
    fontSize = 30
    WhiteColor = (255, 255, 255)
    BlackColor = (0, 0, 0)
    def __init__(self,screen):
        self.screen = screen
        width, height = self.screen.get_size()
        self.defaultSize = (width/3,width/12)
        self.intialPos = (width/2 - self.defaultSize[0]/2,height/2)
        self.defaultMargin = self.defaultSize[1]/3
        pygame.font.init( )
        if not pygame.font.get_init( ):
            raise RuntimeError( "pygame doesn't init" )
        self.myfont = pygame.font.SysFont('Font/Raleway/Raleway-VariableFont_wght.ttf', self.fontSize)
        self.addButton("Continue")
        self.addButton("New Game")
        self.addButton("Quit")
        self.yPosCalc()

    def animate(self):
        self.buttonState(pygame.mouse.get_pos())
        for i in range(len(self.buttonsBoxes)):
            self.drawButton(i)

    def addButton(self,text):
        self.buttonCounter += 1
        x = self.intialPos[0]
        width = self.defaultSize[0]
        height = self.defaultSize[1]
        self.buttonsBoxes.append((x,0,width,height))
        self.buttonsTextes.append(text)
        self.buttonsStates.append(0)
    def yPosCalc(self):
        yInit = self.intialPos[1] - (self.buttonCounter*self.defaultSize[1]+(self.defaultMargin)*(self.buttonCounter-1))/2
        for i in range(len(self.buttonsBoxes)):
            y = yInit + i*(self.defaultMargin + self.defaultSize[1])
            self.buttonsBoxes[i] = (self.buttonsBoxes[i][0],y,self.buttonsBoxes[i][2],self.buttonsBoxes[i][3])         
    def drawButton(self,i):
        if(self.buttonsStates[i] == 0):
            buttonRender = self.myfont.render(self.buttonsTextes[i], True, self.BlackColor)
            width = 0
        else:
            buttonRender = self.myfont.render(self.buttonsTextes[i], True, self.WhiteColor)
            width = 2

        textSize = buttonRender.get_size()
        x = self.buttonsBoxes[i][0]+ self.defaultSize[0]/2 - textSize[0]/2
        y = self.buttonsBoxes[i][1]+ self.defaultSize[1]/2 - textSize[1]/2
        pygame.draw.rect(self.screen,self.WhiteColor,self.buttonsBoxes[i],width)
        self.screen.blit(buttonRender,(x,y))
    
    def buttonState(self,MousePos):
        for i in range(len(self.buttonsBoxes)):
            if(self.isMouseIn(MousePos,i)):
               self.buttonsStates[i] = 1
            else:
               self.buttonsStates[i] = 0

    def right(self,i):
        return self.buttonsBoxes[i][0]+self.buttonsBoxes[i][2]
    def left(self,i):
        return self.buttonsBoxes[i][0]
    def top(self,i):
        return self.buttonsBoxes[i][1]
    def bottom(self,i):
        return self.buttonsBoxes[i][1]+self.buttonsBoxes[i][3]

    def isMouseIn(self,MousePos,i):
        if(MousePos[0] > self.right(i)):
            return False
        if(MousePos[0] < self.left(i)):
            return False
        if(MousePos[1] > self.bottom(i)):
            return False
        if(MousePos[1] < self.top(i)):
            return False
        return True
