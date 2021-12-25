import sys
 
import pygame
from pygame.locals import *
from Background import Background
from Character import Character
from Objects import Objects
 
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
hpos = height*2.6/3
screen = pygame.display.set_mode((width, height))
charact = Character(screen,(0,hpos),height/3)
back = Background(screen,(0,hpos),0.5)
obj = Objects(screen,(width,hpos),0.5)
# Game loop.
i = 0
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN and (event.key == pygame.key.key_code("space") or event.key == pygame.key.key_code("up")) :
      charact.jump()

  
  # Update.
  for hbox in obj.hitBox:
    if( charact.didHit(hbox)):
      print("dead" + str(i))
      i+=1
  # Draw.
  back.animate()
  charact.animate()
  obj.animate()

  pygame.display.flip()
  fpsClock.tick(fps)