# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:23:46 2020

@author: WSX
"""

import pygame 
from pygame.locals import *
import sys


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width, height =500, 600
position = 250, 200
points = [(50, 150), (100, 150), (150, 200), (100, 250), (50, 250)]
points2 = [(i, j+200) for (i, j) in points]
r = 50
pi = 3.14
closing = 0 #画lines是否闭合


screen = pygame.display.set_mode(size)
pygame.display.set_caption('FIG')
                           
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (50, 50, 100, 50), 0)
        pygame.draw.rect(screen, BLACK, (200, 50, 100, 50), 1)
        pygame.draw.rect(screen, BLACK, (350, 50, 100, 50), 10)
        pygame.draw.polygon(screen, BLACK, points, 0)
        pygame.draw.circle(screen, BLACK, position, r, 2)
        pygame.draw.ellipse(screen, BLACK, (350, 175, 100, 50), 1)
        pygame.draw.arc(screen, BLACK, (50, 250, 400, 100), pi, 2*pi, 1)
        pygame.draw.lines(screen, BLACK, closing, points2, 1)
        
        pygame.draw.line(screen, BLACK, (200, 350), (300, 400), 1)
        pygame.draw.aaline(screen, BLACK, (200, 400), (300, 450), 1)#最后一个参数,是否开启抗锯齿
        
        pygame.display.flip()
        
        clock.tick(5)