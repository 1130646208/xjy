# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:52:39 2020

@author: WSX
"""

import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.mixer.init()#可以不写

pygame.mixer.music.load('ice.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

gold_sound = pygame.mixer.Sound('pickupgold.ogg')
gold_sound.set_volume(0.1)

wrong_sound = pygame.mixer.Sound('wrong.ogg')
wrong_sound.set_volume(0.1)




size = width, height = 300, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MUSIC')

pause_img = pygame.image.load('pause.png').convert_alpha()
unpause_img = pygame.image.load('unpause.png').convert_alpha()

pause_rect = pause_img.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) / 2, (height - pause_rect.height) / 2
unpause_rect = unpause_img.get_rect()
unpause_rect.left, unpause_rect.top = (width - unpause_rect.width) / 2, (height - unpause_rect.height) / 2


pause = False
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                gold_sound.play()
            elif event.button == 3:
                wrong_sound.play()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
            if pause:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.play()
                 
    screen.fill((255, 255, 255))
    
    if pause:
        screen.blit(pause_img, pause_rect)
    else:
        screen.blit(unpause_img, unpause_rect)
        
    pygame.display.flip()
    clock.tick(10)
        