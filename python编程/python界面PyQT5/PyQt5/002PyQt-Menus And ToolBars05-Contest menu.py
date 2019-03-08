#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a context menu.
------------------------------------------------------------------------
--      右键菜单：contextMenuEvent()重写该方法：实现这个菜单：
--      action = cmenu.exec_(self.mapToGlobal(event.pos())):
--          使用exec_()：方法显示菜单。
--          从鼠标右键事件对象中获得当前坐标。
--          mapToGlobal()：方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
------------------------------------------------------------------------

"""

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))   # 从鼠标右键事件对象中获得当前坐标event.pos()。
        # mapToGlobal() 把当前组件的相对坐标转换为窗口（window）的绝对坐标。

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

