import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainUI import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.stack_display)
        self.setupUi(self)
        self.Btn1_BaseInfo.clicked.connect(lambda: self.stack_display(0))
        self.Btn2_Backgroud.clicked.connect(lambda: self.stack_display(1))
        self.Btn3_HHIES.clicked.connect(lambda: self.stack_display(2))
        self.Btn4_Estimate.clicked.connect(lambda: self.stack_display(3))

    def stack_display(self, n):
        self.stackedWidget.setCurrentIndex(n)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
