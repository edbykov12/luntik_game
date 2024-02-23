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
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luntik meme adventures")
gameScreen.fill((255,255,255))
pygame.display.flip()
#музычка1
music1=pygame.mixer.music.load("PXLUS - PAIN BRAZIL.mp3")
#music2=pygame.mixer.music.load("Downloads\Telegram Desktop\Неизвестный_исполнитель_Тема_из_пиратов_Карибского_моря_www_hotplayer.mp3")
pygame.mixer.music.play()
# Цикл игры
while 1:
    for i in pygame.event.get():
        pygame.mouse.set_visible
        pygame.mouse
        if i.type == pygame.QUIT:
            sys.exit()
        #if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button==2:
                music1.pause()
                music2.play()
        # Коментарий от женяся:
        # e - это номер уровня на котором игрок остановился т.е надо запускать е-тый уровень) И да код обменника файлами уже написан)

        