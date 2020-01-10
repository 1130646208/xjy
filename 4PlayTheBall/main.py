# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:36:12 2020

@author: WSX
"""

import pygame
from pygame.locals import *
import sys
from random import *
import traceback

#球类
class Ball(pygame.sprite.Sprite):
    def __init__(self, green_ball_image, gray_ball_image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)
        
        self.green_ball_image = pygame.image.load(green_ball_image).convert_alpha()
        self.gray_ball_image = pygame.image.load(gray_ball_image).convert_alpha()
        self.rect = self.green_ball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.side = [1 if self.speed[0] >= 0 else -1, 1 if self.speed[1] >= 0 else -1]
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2 + 5;
        
        self.target = target
        self.control = False
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if self.rect.left >= self.width:
            self.rect.right = 0
        elif self.rect.right <= 0:
            self.rect.left = self.width
        if self.rect.top >= self.height:
            self.rect.bottom = 0
        elif self.rect.bottom <= 0:
            self.rect.top = self.height
            
    def check(self, motion):
        if self.target - 5 < motion < self.target + 5:
            return True
        else:
            return False

#玻璃面板类
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        
        self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) // 2,\
                                        bg_size[1] - self.glass_rect.height

        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top
        pygame.mouse.set_visible(False)
        
def main():
    pygame.init()
    
    #添加图片
    green_ball_image = 'green_ball.png'
    gray_ball_image = 'gray_ball.png'
    bg_image = 'bg.png'
    glass_image = 'glass.png'
    mouse_image = 'hand.png'
    useless_image = 'useless.png'
    #添加音乐
    pygame.mixer.music.load('gaming2.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    
    
    #添加音效
    hole_sound = pygame.mixer.Sound('hole.ogg')
    hole_sound.set_volume(0.1)
    
    win_sound = pygame.mixer.Sound('win.ogg')
    win_sound.set_volume(0.1)
    
    fail_sound = pygame.mixer.Sound('fail.ogg')
    fail_sound.set_volume(0.1)
    
    laugh_sound = pygame.mixer.Sound('laugh.ogg')
    laugh_sound.set_volume(0.1)
    
    #音乐播放完,游戏结束
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)#发送到消息队列中
    
    #指定窗口标题,背景,宽高,键盘重复响应速度
    bg_size = width, height = 1024, 511
    screen = pygame.display.set_mode(bg_size)
    background = pygame.image.load(bg_image).convert_alpha()
    pygame.display.set_caption('PLAY THE BALL!')
    
    pygame.key.set_repeat(100, 100)#第一个参数代表第一次发送事件的延迟,第二个参数指定重复发送事件的时间间隔,无参数表示取消重复发送
    
    #存放小球的列表
    balls = []
    group =pygame.sprite.Group()
    #使用spritecollide方法,需要使用sprite.Group()
    #spritecollide(sprite, group, dokill, collide = None),第三个参数是是否从组中删除,第四个是碰撞检测方法
    
    #洞
    holes = [(154,158,221,225),(367,371,92,96),(467,471,334,338),\
             (770,774,343,347),(831,835,143,147)]
    #消息队列
    msgs = []
    #实例化小球,并加入碰撞检测
    for i in range(5):
        position = randint(0, width-50), randint(0, height-50)
        speed = [randint(-5, 5), randint(-5, 5)]
        ball = Ball(green_ball_image, gray_ball_image, position, speed, bg_size, 6 * (i+1))
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width-50), randint(0, height-50)
            
        balls.append(ball)
        group.add(ball)
    #实例化玻璃
    glass = Glass(glass_image, mouse_image, bg_size)
    
    motion = 0
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1 * 1000)   
    
    #运行起来
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == GAMEOVER:
                fail_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False
            elif event.type == MYTIMER:
                if motion:
                    print(motion)
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0
            elif event.type == MOUSEMOTION:
                motion += 1
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1
                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in holes:
                                if i[0] <= each.rect.centerx <= i[1] and i[2] <= each.rect.centery <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0, 0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0, temp)
                                    holes.remove(i)
                            if not holes:
                                pygame.mixer.music.stop()
                                win_sound.play()
                                msg = pygame.image.load(useless_image).convert_alpha()
                                msg_pos = (width - msg.get_width()) // 2, (height - msg.get_height()) // 2
                                msgs.append((msg, msg_pos))
                                laugh_sound.play()
  
        #绘制背景
        screen.blit(background, (0, 0))
        #绘制玻璃,指针
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.right > glass.glass_rect.right:
            glass.mouse_rect.right = glass.glass_rect.right
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.bottom > glass.glass_rect.bottom:
            glass.mouse_rect.bottom = glass.glass_rect.bottom
         
        screen.blit(glass.glass_image, glass.glass_rect)
        screen.blit(glass.mouse_image, glass.mouse_rect)
        #绘制小球
        for each in balls: 
            each.move()
            if each.control == True:
                screen.blit(each.gray_ball_image, each.rect)
            else:
                screen.blit(each.green_ball_image, each.rect)
            
         #碰撞检测   
        for each in group:
            group.remove(each) 
            
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.side = [1 if each.speed[0] >= 0 else -1, 1 if each.speed[1] >= 0 else -1]
                each.speed = [randint(1, 5)*(-each.side[0]), randint(1, 5)*(-each.side[1])]
                each.control = False
            group.add(each)
                 
        #打印消息
        for msg in msgs:
            screen.blit(msg[0], msg[1])
        #图像显示到屏幕上
        pygame.display.flip()
        clock.tick(30)
                 
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()