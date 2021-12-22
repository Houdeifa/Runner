import sys
 
import pygame
from pygame.locals import *

from Ressources import Ressources
 
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
res = Ressources(0.2)

i = 0
speed = 0.4
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  
  # Update.

  # Draw.
  screen.blit(res.RunImgs[int(i)], (0,0))
  i+=speed
  if(i > 7):
    i = 0
  pygame.display.flip()
  fpsClock.tick(fps)