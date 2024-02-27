import random
import time
import PyQt6
import pygame
import sys

f = open('checkpoint.txt', 'r')
e = f.read()
f.close()
pygame.init()
gameScreen = pygame.display.set_mode((400, 300))
# Модуль os - позиция окна
import os
x = 100
y = 100
os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
# Параметры окна
size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luntik meme adventures")
gameScreen.fill((255,255,255))
pygame.display.flip()
#музычка
music1=pygame.mixer.music.load("PXLUS - PAIN BRAZIL.mp3")
pygame.mixer.music.play()
#Иконка
img=pygame.image.load("мия.jpg")
pygame.display.set_icon(img)
#Цикл Игры
while 1:
    for i in pygame.event.get():
        pygame.mouse.set_visible
        pygame.mouse
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button==1:
               music2=pygame.mixer.music.load("Пираты Карибского моря.mp3")
               pygame.mixer.music.play()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button==3:
               music2=pygame.mixer.music.load("PXLUS - PAIN BRAZIL.mp3")
               pygame.mixer.music.play()
        if i.type ==  pygame.MOUSEBUTTONDOWN:
            if i.button==2:
                music3=pygame.mixer.music.load('Ravilz Toothless Dancing.mp3')  
                pygame.mixer.music.play()