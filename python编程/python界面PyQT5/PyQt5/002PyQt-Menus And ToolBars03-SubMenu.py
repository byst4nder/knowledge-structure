#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This program creates a submenu and action.
--------------------------------------------------------------
    addMenu(QMenu)
    addAction(QAction())
----------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')   # 在菜单栏添加新菜单。

        impMenu = QMenu('Import', self)    # 使用QMenu创建一个新菜单。
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 过程梳理：
    # S1:使用menubar.addMenu('File')在菜单栏添加file菜单项目fileMenu(这个一级父菜单)
    # S2:使用QMenu('Import', self) 创建一个新的菜单impMenu（这个二级子菜单）
    # S3:QAction()创建菜单栏、工具栏或者快捷键的动作组合impAct
    # S4:将这个动作impAct添加给二级子菜单impMenu ====>>>> impMenu.addAction(impAct)
    # S5:将这个附有动作impAct的二级子菜单impMenu，加到一级父菜单fileMenu下面。fileMenu.addMenu(impMenu)

    # S6:我们也可以给一级父菜单加个动作,先创建动作：newAct=QAction("new", self).
    # S7:然后动作加到一级父菜单下面：

    # 牢记，一级菜单下面可以加动作，也可以加菜单：
    #   1、addAction(QAction())
    #   2、addMenu(QMenu())



