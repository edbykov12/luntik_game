import sys
import pygame
from PyQt6.QtCore import QSize, Qt, QRect, QPoint
from PyQt6.QtGui import QIcon, QAction, QColor, QPixmap, QFont, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGraphicsColorizeEffect, QToolBar, QSlider, \
QWidget, QVBoxLayout, QHBoxLayout, QFileDialog

import os


app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создаем панель основного меню
        
        main_menu = self.menuBar()
        # Добавляем в него меню actions
        file_menu = main_menu.addMenu("МЕНЮ")
        y = QAction("Магазин", self)
        yy = QAction("Инвентарь", self)
        yyy = QAction("Уровни", self)
        yyyy = QAction("Сохранить игру", self)
        self.yyyyy = QAction("Загрузить игру", self)
        file_menu.addAction(y)
        file_menu.addAction(yy)
        file_menu.addAction(yyy)
        file_menu.addAction(yyyy)
        file_menu.addAction(self.yyyyy)
        self.yyyyy.triggered.connect(self.z)


    def z(self):
        import luntus
            

window = MainWindow()
window.setWindowTitle("Luntik meme adventures")
window.setGeometry(100,100,100,100)
window.show()
app.exec()
