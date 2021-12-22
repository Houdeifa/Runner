import pygame
class Ressources:
    RunImgs = []
    IDLEImgs = []
    JumpImgs = []

    def __init__(self,scale=1):
        for i in range(8):
         self.RunImgs.append(pygame.image.load('Adventure Girl/png/Run ('+ str(i+1) +').png'))
         size = self.RunImgs[i].get_size()
         self.RunImgs[i] = pygame.transform.scale(self.RunImgs[i], (int(size[0]*scale), int(size[1]*scale)))
        
        for i in range(10):
         self.IDLEImgs.append(pygame.image.load('Adventure Girl/png/Idle ('+ str(i+1) +').png'))
         size = self.IDLEImgs[i].get_size()
         self.IDLEImgs[i] = pygame.transform.scale(self.IDLEImgs[i], (int(size[0]*scale), int(size[1]*scale)))
        
        for i in range(10):
         self.JumpImgs.append(pygame.image.load('Adventure Girl/png/Jump ('+ str(i+1) +').png'))
         size = self.JumpImgs[i].get_size()
         self.JumpImgs[i] = pygame.transform.scale(self.JumpImgs[i], (int(size[0]*scale), int(size[1]*scale)))
        
    
    