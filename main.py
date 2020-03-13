import pygame
import keyboard
import time
from pygame.locals import *

pygame.init()

pygame.key.set_repeat(100, 25)
continuer = True
screensize = (1280, 720)
fenetre = pygame.display.set_mode(screensize, RESIZABLE)

fond = pygame.image.load("fond.jpg").convert_alpha()
white = Color(0,0,0)
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text,a,b):
    largeText = pygame.font.Font('comicsans.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (a,b)
    fenetre.blit(TextSurf, TextRect)


while continuer :

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()



    fenetre.blit(fond, (0,0))
    message_display("wesh les gens", 50, 50)


    pygame.time.Clock().tick(120)
    pygame.display.update()






