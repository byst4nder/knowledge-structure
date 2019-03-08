#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This program centers a window
on the screen.
---------------------------------------------------------------------------
--      qr = self.frameGeometry()   # 得到了主窗口的大小。
--      cp = QDesktopWidget().availableGeometry().center()  # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
--      qr.moveCenter(cp)
---------------------------------------------------------------------------
"""


import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(500, 309)
        self.center()   # 这个方法是调用我们下面写的，实现对话框居中的方法。

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()   # 得到了主窗口的大小。

        cp = QDesktopWidget().availableGeometry().center()  # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
# qr = self.frameGeometry()得到了主窗口的大小。
# 区分：frameGeometry()和geometry()：一个是窗口大小，一个是用户区大小。
    # frameGeometry()是整个外部窗口的大小。轮廓的大小。等同QWidget中的x.(),y.()，都是获取界面包括标题栏顶最左上角的x和y轴坐标。
    # 01中有w=QWidget(),w.resize()

    # geomatry中的x.(),y.()获取的坐标是不包括标题栏最左上角位置（在此叫用户区），
    # 同样geometry()中的width()和height()获取的也是用户区中的宽度和高度。归根结底是用于获取用户区域的坐标信息。


# cp = QDesktopWidget().availableGeometry().center()  1、获取显示器的分辨率，2、然后得到中间点的位置。

# qr.moveCenter(cp)
# 然后把自己窗口的中心点放置到qr的中心点。
# self.move(qr.topLeft())
# 然后把窗口的坐上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了。

# cp是屏幕中心点，qr是构建的主窗口方框。 窗口的移动，既要中心，又要topLeft
    # S1:先将qr的主窗口中心移动到中心，
    # S2:将主窗口qr的左上角TopLeft（初始点）移动到方框的左上角。对齐。
