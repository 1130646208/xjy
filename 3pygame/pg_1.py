# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:39:37 2020

@author: WSX
"""
import pygame
import sys
from pygame.locals import *
#init pygame

pygame.init()
print('support solutions:', pygame.display.list_modes())

size = width, height = 600, 400
fullscreen = False
speed = [-2, 1]
bg = (255, 255, 255)

#create window
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size, RESIZABLE)#setmode 返回surface对象

#set window title

pygame.display.set_caption('GAMEING...')

#load picture

ohero = pygame.image.load('hero.jpg')
r_head = ohero
hero = l_head = pygame.transform.flip(ohero, True, False)

ratio = 1.0
#get location of image
ohero_rect = position = ohero.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                hero = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                speed = [1, 0]
                hero = r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
            #全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    size = width, height = 1920, 1080
                    screen = pygame.display.set_mode(size, FULLSCREEN | HWSURFACE)
                else:
                    size = width, height = 600, 400
                    screen = pygame.display.set_mode(size, RESIZABLE)
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1
                hero = pygame.transform.smoothscale(ohero, \
                                                      (int(ohero_rect.width * ratio), \
                                                      int(ohero_rect.height * ratio)))
                r_head = hero
                l_head = pygame.transform.flip(hero, True, False)
                
       
        if event.type == VIDEORESIZE and size != (1920, 1080):
            size = event.size
            width, height = size
            print('resize:', size)
            pygame.display.set_mode(size, RESIZABLE)
            
    #move image
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #filp image
        hero = pygame.transform.flip(hero, True, False)
        speed[0] = -speed[0]


    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #fill background
    screen.fill(bg)
    #refresh image
    screen.blit(hero, position)
    #上↑双缓冲机制
    
    #refresh window
    pygame.display.flip()

    #two methods to control game speed
    #pygame.time.delay(10)#delay ms
    clock.tick(100)
    
