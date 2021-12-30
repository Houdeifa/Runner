import sys
 
import pygame
from pygame.locals import *
from GameManager import GameManager
 
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
gameMan = GameManager(screen)
# Game loop.
i = 0
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN and (event.key == pygame.key.key_code("space") or event.key == pygame.key.key_code("up")) :
      gameMan.charact.jump()
    elif event.type == pygame.MOUSEBUTTONUP:
      gameMan.MouseClick()

  
  # Update.
  gameMan.checkLoose()
  # Draw.
  gameMan.animate()
  pygame.display.flip()
  fpsClock.tick(fps)