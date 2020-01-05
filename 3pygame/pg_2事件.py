# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:39:37 2020

@author: WSX
"""
import pygame
import sys
#初始化Pygame
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('event')
bg = (0, 0, 0)

position = 0


font = pygame.font.Font(None, 20)
lineheight = font.get_height()
screen.fill(bg)

f = open('record.txt', 'w')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        fontscreen = font.render(str(event), True, (0, 255, 0))#参数1将event转化成的字符串渲染,参数2抗锯齿
        screen.blit(fontscreen, (0, position))
        position += lineheight
        if  position > height:
            position = 0
            screen.fill(bg)
            
    pygame.display.flip()