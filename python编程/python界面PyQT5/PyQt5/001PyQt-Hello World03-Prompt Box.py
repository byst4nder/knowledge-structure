#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 提示框,并设置悬浮提示内容。

"""
This example shows a tooltip on
a window and a button.
---------------------------------------------------------------------------
--      btn = QPushButton('Button', self)   # 创建按钮，下面并给按钮一个提示。
--      btn.setToolTip('This is a <b>QPushButton</b> widget')
--
--      setToolTip()
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):   # 使用initUI()方法创建一个GUI。

        QToolTip.setFont(QFont('SansSerif', 10))   # 静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。

        # self.setToolTip('This is a <b>QWidget</b> widget')  # 可有可无

        btn = QPushButton('Button', self)   # 创建一个按钮
        btn.setToolTip('This is a <b>QPushButton</b> widget')   # 创建一个按钮提示框，当鼠标悬浮于按钮时，提示内容。
        # btn.resize(btn.sizeHint())
        # btn.resize(btn.sizeHint())
        # btn.resize(QSize(500, 309))
        btn.resize(200, 123)
        btn.move(110, 50)

        self.setGeometry(300, 220, 960, 700)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 为应用创建了一个提示框。
# QToolTip.setFont(QFont('SansSerif', 10))
# 这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。

# self.setToolTip('This is a <b>QWidget</b> widget')
# 调用setTooltip()创建提示框可以使用富文本格式的内容。

# btn = QPushButton('Button', self)
# btn.setToolTip('This is a <b>QPushButton</b> widget')
# 创建一个按钮，并且为按钮添加了一个提示框。

# btn.resize(btn.sizeHint())
# btn.move(50, 50)
# 调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。


# 强调：
#     通过以上代码：为新的App创建了两个ToolTip，当鼠标悬停在主界面或按钮时就会显示指定的内容。
