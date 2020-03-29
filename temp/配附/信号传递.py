# 通过lambda也是一种定义的函数：来实现对重复函数的缩减。取代槽函数。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainUI import Ui_MainWindow


# 写法一：直白的写法。
# class MyMainWindow(QMainWindow, Ui_MainWindow):
#
#     def __init__(self, parent=None):
#         super(MyMainWindow, self).__init__(parent)
#         # self.ui = Ui_MainWindow()
#         # self.ui.setupUi(self)
#         # self.ui.pushButton.clicked.connect(self.stack_display)
#         self.setupUi(self)
#         self.Btn1_BaseInfo.clicked.connect(self.stack1_display)
#         self.Btn2_Backgroud.clicked.connect(self.stack2_display)
#         self.Btn3_HHIES.clicked.connect(self.stack3_display)
#         self.Btn4_Estimate.clicked.connect(self.stack4_display)
#
#     def stack1_display(self):
#         self.stackedWidget.setCurrentIndex(0)
#
#     def stack2_display(self):
#         self.stackedWidget.setCurrentIndex(1)
#
#     def stack3_display(self):
#         self.stackedWidget.setCurrentIndex(2)
#
#     def stack4_display(self):
#         self.stackedWidget.setCurrentIndex(3)


# 写法二：带参数的槽函数：通过lambda实现：
class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.stack_display)
        self.setupUi(self)
        self.Btn1_BaseInfo.clicked.connect(lambda: self.leftBtnShow(0))
        self.Btn2_Backgroud.clicked.connect(lambda: self.leftBtnShow(1))
        self.Btn3_HHIES.clicked.connect(lambda: self.leftBtnShow(2))
        self.Btn4_Estimate.clicked.connect(lambda: self.leftBtnShow(3))

    def leftBtnShow(self, n):
        self.stackedWidget.setCurrentIndex(n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
