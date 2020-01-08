# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:36:12 2020

@author: WSX
"""

import pygame
from pygame.locals import *
import sys
from random import *
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left > self.width:
            self.rect.left = 0
        elif self.rect.right < 0:
            self.rect.right = self.width
        elif self.rect.top > self.height:
            self.rect.top = 0
        elif self.rect.bottom <0:
            self.rect.bottom = self.height
            
def collide_check(ball, target):
    
    collide_ones = []
    
    for each in target:
        distance = math.sqrt(pow((each.rect.center[0]-ball.rect.center[0]), 2) + \
                        pow((each.rect.center[1]-ball.rect.center[1]), 2))
        if distance <= (each.rect.width + ball.rect.width) / 2:
            collide_ones.append(each)
            
    return collide_ones


def main():
    pygame.init()
    
    ball_image = 'ball.png'
    bg_image = 'bg.png'
    bg_size = width, height = 1024, 511
    
    screen = pygame.display.set_mode(bg_size)
    background = pygame.image.load(bg_image).convert_alpha()
    pygame.display.set_caption('PLAY THE BALL!')
    

    balls = []
    BALL_NUM = 5
    
    for i in range(BALL_NUM):
        position = randint(0, width-50), randint(0, height-50)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        
        while collide_check(ball, balls):
            ball.rect.left, ball.rect.top = randint(0, width-50), randint(0, height-50)
            
        balls.append(ball)
        
    
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(background, (0, 0))
        
        for i in range(BALL_NUM):
            ball = balls.pop(i)
            
            if collide_check(ball, balls):
                ball.speed[0] = -ball.speed[0]
                ball.speed[1] = -ball.speed[1]       
            balls.insert(i, ball)
        
        for each in balls: 
            each.move()
            screen.blit(each.image, each.rect)
            
        
            
            
        pygame.display.flip()
        clock.tick(30)
    
    


if __name__ == '__main__':
    main()