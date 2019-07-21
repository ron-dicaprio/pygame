import pygame
import os
from pygame.locals import *
'''
white = (255,255,255)
black= (0,0,0)
pygame.mixer.music.load(r'd:\\spy\\ZB_BGM1.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.50)
'''
os.environ['SDL_VIDEO_CENTERED'] = '1'  #窗口居中
pygame.display.set_caption('菜芽豆与黄花菜的故事')
game_scr = pygame.display.set_mode((1024,461),0,32) #必须先定义视窗
BG_Pic = pygame.image.load(r'd:\\spy\\ZB01.jpg').convert()
shooter = pygame.image.load(r'd:\\spy\\sunf.gif').convert_alpha()
pygame.init()
while True:
    game_scr.blit(BG_Pic,(0,0))
    x,y = pygame.mouse.get_pos()  #获取鼠标位置
    x = x - shooter.get_width() / 2
    y = y - shooter.get_height() / 2
    game_scr.blit(shooter,(x,y))
    for event in pygame.event.get():#event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #easygui.msgbox('lol')
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                click_x,click_y = pygame.mouse.get_pos()
                click_x = click_x - shooter.get_width()/2
                click_y = click_y - shooter.get_height()/2
                game_scr.blit(shooter,(click_x,click_y))
                print('ok')
        break
    pygame.display.update()
    pygame.time.delay(10)
