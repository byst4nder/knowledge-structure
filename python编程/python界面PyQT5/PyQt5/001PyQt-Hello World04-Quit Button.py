#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 退出按钮

"""
This program creates a quit
button. When we press the button,
the application terminates.

---------------------------------------------------------------------------
--      qbtn = QPushButton('Quit', self)   # 按钮显示“quit”
--      qbtn.clicked.connect(QCoreApplication.instance().quit)
--      按钮点击操作，触发事件操作。
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self)   # 按钮显示“quit”
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        qbtn.resize(200, 100)
        qbtn.move(400, 500)

        self.setGeometry(300, 220, 960, 700)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# qbtn.clicked.connect(QCoreApplication.instance().quit)
# 事件传递系统在PyQt5内建的single和slot机制里面。
# 点击按钮之后，信号会被捕捉并给出既定的反应。
# QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
# QCoreApplication是在QApplication里创建的。点击事件和能终止进程并退出应用的quit函数绑定在了一起。
# 在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。





