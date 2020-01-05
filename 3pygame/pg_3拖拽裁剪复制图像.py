# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:56:57 2020

@author: WSX
"""
import pygame
import sys
from pygame.locals import *#导入键位等变量

pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('切图器')


turtle = pygame.image.load('hero.jpg')
#  0 未开始 1 正在 2 完成
drag = 0
select = 0


position = turtle.get_rect()
position.center = width //2, height //2

select_rect = pygame.Rect(0, 0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
            #第一次点击,选择范围
                if select == 0 and drag == 0:
                    pos_start = event.pos
                    select = 1

            #第二次点击,拖拽图像
                elif select == 2 and drag == 0:
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                    drag = 1
                
            #第三次点击,初始化
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0
                
                
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                #第一次释放,选择结束
                if select == 1 and drag == 0:
                    select = 2
                    pos_stop = event.pos
                #第二次释放,结束拖拽
                if select == 2  and drag == 1:
                    drag = 2
                
        screen.fill(bg)
        screen.blit(turtle, position)
        if select:
            mouse_pos = pygame.mouse.get_pos()
            if select == 1:
                pos_stop = mouse_pos
                
            select_rect.left, select_rect.top = pos_start
            select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
            
            pygame.draw.rect(screen, (0, 0, 0), select_rect, 1)
            
        #拖拽裁剪的图像
        if drag:
            if drag == 1:
                cap_rect.center = mouse_pos
            screen.blit(capture, cap_rect)
                
        pygame.display.flip()
        
        clock.tick(30)