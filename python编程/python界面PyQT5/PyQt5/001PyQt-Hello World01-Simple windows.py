#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
we create a simple window in PyQt5.

---------------------------------------------------------------------------
--      w = QWidget()
--      w.resize()
--      w.move()
--
--      app = QApplication(sys.argv)
---------------------------------------------------------------------------
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()       # 实例化构造一个窗口（window）
    w.resize(960, 700)    # 整个窗口大小
    w.move(300, 200)      # 左上角移动多少，窗口打开初始位置
    w.setWindowTitle('Simple')     # 窗口标题
    w.show()        # 开始显示

    sys.exit(app.exec_())

# from PyQt5.QtWidgets import QApplication, QWidget
    # 引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。
    # widget:小器具，装饰品，窗口小部件

# app = QApplication(sys.argv)
    # 每个PyQt5应用都必须创建一个应用对象。
    # sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。

# w = QWidget()
    # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
    # 默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。

# sys.exit(app.exec_())
    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。
    # sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。





