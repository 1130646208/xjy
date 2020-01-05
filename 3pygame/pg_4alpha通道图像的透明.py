# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:33:08 2020

@author: WSX
"""

import pygame
import sys
from pygame.locals import *


pygame.init()

size = width, height = 600, 400
bg = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('透明')

#hourse = pygame.image.load('hourse.png').convert()
hourse = pygame.image.load('hourse.png').convert_alpha()

background = pygame.image.load('background.jpg')
position = hourse.get_rect()
position.center = width // 2, height // 2

hourse.set_colorkey((255, 255, 255))
#hourse.set_alpha(20)  #带alpha通道的surface不能调用set_alpha设置alpha大小

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0, 0))
    #screen.blit(hourse, position)
    blit_alpha(screen, hourse, position, 100)
    pygame.display.flip()
    
    clock.tick(30)