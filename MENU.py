# import sys
# import pygame
# from PyQt6.QtCore import QSize, Qt, QRect, QPoint
# from PyQt6.QtGui import QIcon, QAction, QColor, QPixmap, QFont, QPainter
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGraphicsColorizeEffect, QToolBar, QSlider, \
# QWidget, QVBoxLayout, QHBoxLayout, QFileDialog


f = open("levels.txt","w+")
if "".join(f.readlines()) != '': 
    e = int("".join(f.readline()))
    f.seek(0)
    f.write(e+1)
    f.close()
elif "".join(f.readlines()) == '':
    f.write("1")
    f.close()



