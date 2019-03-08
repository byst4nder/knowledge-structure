#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows an icon
in the titlebar of the window.

---------------------------------------------------------------------------
--        self.initUI()
--        self.setGeometry(300, 220, 960, 700)
--        self.setWindowIcon(QIcon('./images/web.jpg'))
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 220, 960, 700)    # 先move()和后resize()的合体。
        self.setWindowTitle('Icon')             # 窗口标题
        # self.setWindowIcon(QIcon('web.png'))  # 窗口小标签图片
        self.setWindowIcon(QIcon('./images/web.jpg'))    # 窗口小标签图片
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # 每个PyQt5应用都必须创建一个应用对象。
    # sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。
    ex = Example()    # 示例对象创立，主循环开始。
    sys.exit(app.exec_())

# 01simple windows是过程式编程，02window icon是面向对象的编程。
# 面向对象编程最重要的三个部分是类（class）、数据和方法。


# class Example(QWidget):创建了一个类的调用，这个类继承自QWidget。
    # 这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。
    #   super()构造器方法返回父级的对象。
    #   __init__()方法是构造器的一个方法。


# self.initUI():使用initUI()方法创建一个GUI。
# 自己准备一个web.png
# self.setGeometry(300, 300, 300, 220)
# self.setWindowTitle('Icon')
# self.setWindowIcon(QIcon('web.png'))
    # 上面的三个方法都继承自QWidget类。
    # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。
    # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
    # 最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。
