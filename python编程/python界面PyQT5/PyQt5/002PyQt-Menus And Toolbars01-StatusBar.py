#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A statusbar is a widget
that is used for displaying status information.
This program creates a statusbar.

---------------------------------------------------------------------------
--      状态栏是由类QMainWindow创建的，继承自QMainWindow类。
--      self.statusBar().showMessage('Ready')  # 调用QtGui.QMainWindow类的statusBar()方法创建状态栏。
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')  # 调用QtGui.QMainWindow类的statusBar()方法创建状态栏。
        # showMessage()方法在状态栏显示内容。

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 状态栏是由类QMainWindow创建的。



