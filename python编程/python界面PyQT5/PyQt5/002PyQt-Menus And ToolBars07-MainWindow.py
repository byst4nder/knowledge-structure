#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This program creates a skeleton(骨架) of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget.

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()     # 文本编辑区域。
        self.setCentralWidget(textEdit)  # 放置在中间区域。

        exitAct = QAction(QIcon('./images/exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')    # added statusTip S1:
        exitAct.triggered.connect(self.close)

        self.statusBar()   # added statusTip S2：

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.setWindowIcon(QIcon('./images/web.jpg'))
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
