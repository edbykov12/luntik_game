import random
import time
import PyQt6
import pygame
import sys
f = open('checkpoint.txt', 'r')
e = f.read()
f.close()
pygame.init()
lvlnmb=e
#Время перезарядки у всех персов одинаковое
atack_time_norm=0.1
if lvlnmb==e:
    #Характеристики врага(в данном случае босс=Шнюк)
    health_agro=1000
    atack_agro=50
    atcack_time_agro=0.3
#Здесь должно быть окно выбора перса
#Пока выбор персонажа будет просто переменная чтобы не выдавыло ошибок
sk_charachter='Дарт Лунтус'
charachter='Лунтик'
if charachter=='Лунтик' and sk_charachter=='Дарт Лунтус':
    health_norm=5000
    shield_norm=100
    atack_norm=300
    super_norm=1000
    super_time_norm=20.0
if charachter=='Деда Шер' and sk_charachter=='Киборг Шер':
    health_norm=3000
    shield_norm=35
    atack_norm=50
    super_norm=385
    super_time_norm=15.0
if charachter=='Баба Капа' and sk_charachter=='Учитель по информатеке Капа':
    health_norm=3500
    shield_norm=75
    atack_norm=65
    super_norm=500
    super_time_norm=17.0
if charachter=='Пчела мен' and sk_charachter=='Антивирус Пчела мен':
    health_norm=2750
    shield_norm=80
    atack_norm=40
    #У этого скина ульта-хилить
    super_norm=75
    super_time_norm=15.0
#Цикл уровня
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
gameScreen.fill((255,255,0))
pygame.display.flip()
img=pygame.image.load("мия.jpg")
pygame.display.set_icon(img)
#музычка
music1=pygame.mixer.music.load("Пираты Карибского моря.mp3")
pygame.mixer.music.play()
#Цикл уровня
while 1:
    for i in pygame.event.get():
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render(str(health_agro), 1, (0, 0, 0))
        gameScreen.blit(text1, (5, 50))
        pygame.display.update()
        if health_agro<=0:
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Поздравляю! Победа!', 1, (180, 0, 0))
            gameScreen.blit(text1, (10, 50))
            pygame.display.update()
            pygame.time.delay(600)
            sys.exit()
        if health_norm<=0:
            music4=pygame.mixer.music.load("ДИМОООН-ДИМОООН_(muzmo.su).mp3")
            pygame.mixer.music.play()
            f2 = pygame.font.Font(None, 36)
            text2 = f2.render('К сожалению вы проиграли...', 1, (180, 0, 0))
            gameScreen.blit(text2, (10, 50))
            wait(6000)
            sys.exit()
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type==pygame.KEYDOWN:
            if i.key== pygame.K_w:
                health_agro=health_agro-atack_norm
    



    

    