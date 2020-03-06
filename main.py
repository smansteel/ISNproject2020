import pygame
import keyboard
import time
from pygame.locals import *

pygame.init()
pygame.time.Clock().set(120)
pygame.set.repeat(100, 25)
continuer = True

while continuer :

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()




