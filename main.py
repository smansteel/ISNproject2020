import pygame
import keyboard
import time
import codecs
import random
from pygame.locals import *

i=200
pygame.init()
liste_mot = ['']
pygame.key.set_repeat(100, 25)
continuer = True
screensize = (1280, 720)
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
mot = [""]
fond = pygame.image.load("fond.jpg").convert_alpha()
white = Color(255,255,255)
green = Color(255,0,0)
u=0

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text,a,b):
    largeText = pygame.font.Font('comicsans.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (a,b)
    fenetre.blit(TextSurf, TextRect)


with codecs.open("words.txt", "r", encoding = "utf-8") as words:
    for mots in words:
        mot = mots.split("\n")
        liste_mot += mot

print(liste_mot)'''
while continuer :

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()


    fenetre.blit(fond, (0,0))
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        key_name = pygame.key.name(event.key)
        if pygame.key.get_focused() == True :
            if event.type == pygame.KEYDOWN:
                message_display('{}'.format(key_name), 10, 20)



    pygame.time.Clock().tick(60)
    pygame.display.update()






