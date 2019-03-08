#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program shows a confirmation
message box when we click on the close
button of the application window.
---------------------------------------------------------------------------
--        reply = QMessageBox.question(self, 'Message',
--                   "Are you sure to quit?", QMessageBox.Yes |
--                     QMessageBox.No, QMessageBox.No)
---------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 220, 960, 700)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否者就忽略关闭事件。
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 如果关闭QWidget，就会产生一个QCloseEvent。改变控件的默认行为，就是替换掉默认的事件处理。


# 重点强调：
# reply= QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
# 我们创建了一个消息框，上面有俩按钮：Yes和No.
# 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。
# 返回值在变量reply里。



