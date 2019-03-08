#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This program creates a menubar. The
menubar has one menu with an exit action.

We create a menubar with one menu. This menu will contain one action which will terminate the application if selected.
A statusbar is created as well. The action is accessible with the Ctrl+Q shortcut.

---------------------------------------------------------------------------
--      act = QAction():创建动作（操作）组合
--      act.setShortcut:动作快捷键
--     act.setStatusTip:动作状态提示
--
--      menubar = self.menuBar()  实例化菜单栏：
--     fileMenu = menubar.addMenu('File')   addMenu:添加 File 菜单
--      fileMenu.addAction  给菜单添加动作。
--      exitAct.triggered.connect(qApp.quit)  动作触发事件。
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('./images/exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。
        # 前面两行，我们创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作。
        # 第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。

        exitAct.triggered.connect(qApp.quit)
        # 当执行这个指定的动作时，就触发了一个事件。
        # 这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。
        self.statusBar()

        menubar = self.menuBar()    # 创建菜单栏
        fileMenu = menubar.addMenu('&File')  # 并在菜单栏上面添加了一个file菜单
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 图标网站：
# http://pngimg.com/imgs/symbols/exit/


