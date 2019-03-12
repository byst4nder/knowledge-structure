#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This example shows a QSlider widget.

"""

from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)

        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('./images/mute.png'))
        # self.label.setGeometry(160, 40, 80, 30)
        self.label.setGeometry(160, 40, 1200, 600)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            # self.label.setPixmap(QPixmap('mute.png'))
            self.label.setPixmap(QPixmap('./images/mute1.png'))
        elif value > 0 and value <= 30:
            # self.label.setPixmap(QPixmap('min.png'))
            self.label.setPixmap(QPixmap('./images/low1.png'))

        elif value > 30 and value < 80:
            # self.label.setPixmap(QPixmap('med.png'))
            self.label.setPixmap(QPixmap('./images/high1.png'))

        else:
            # self.label.setPixmap(QPixmap('max.png'))
            self.label.setPixmap(QPixmap('./images/9207.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
