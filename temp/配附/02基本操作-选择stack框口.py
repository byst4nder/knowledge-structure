# 通过mainUI.ui已经搭建好主程序的界面：下面分步来实现所有功能。
# S1:首先实现通过点击左侧btn来切换右侧窗口显示功能。
#       新建一个窗口开始测试：保存为BtnChangeStackedWidget.ui
#       搭建好ui，转换为python文件，拷贝到当前测试路径下，等待主界面调取。
#       转入python编辑。
#       将业务逻辑写在此处来实现调用。
#       如下直接连接slot和signal即可。


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from BtnChangeStackedWidget import Ui_MainWindow
# from PyQt5.QtCore import pyqtSignal, Qt


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.stack_display)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.stack1_display)
        self.pushButton_2.clicked.connect(self.stack2_display)
        self.pushButton_3.clicked.connect(self.stack3_display)

    def stack1_display(self):
        self.stackedWidget.setCurrentIndex(0)

    def stack2_display(self):
        self.stackedWidget.setCurrentIndex(1)

    def stack3_display(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
