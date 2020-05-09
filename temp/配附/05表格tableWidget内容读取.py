# 通过之前获取children()来解决列表问题，现在通过toggled()状态切换触发来执行读取内容。解决返回值为空问题。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget
from 配附.InputEdit import Ui_Form
import numpy as np
# https://my.visualstudio.com/Downloads?q=visual%20studio%202017&wt.mc_id=o~msft~vscom~older-downloads


class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Info_dict = {"baseInfo": {}, "bg_info": {}}
        # print(self.tableWidget.rowCount())
        # print(self.groupBox_3.title())
        # print(self.groupBox_3.findChild(QTableWidget))
        self.saveTest(self.tableWidget)

    def saveTest(self, tableWidgetName):
        self.pushButton_3.clicked.connect(lambda: self.readTable(tableWidgetName))

    def readTable(self, tableWidgetName):
        print("保存按钮被点击")
        checkBoxMat = np.zeros((tableWidgetName.rowCount(), tableWidgetName.columnCount()), dtype=str)
        print(checkBoxMat)
        for i in range(tableWidgetName.rowCount()):
            for j in range(tableWidgetName.columnCount()):
                if tableWidgetName.item(i, j) is None:
                    checkBoxMat[i, j] = 0

                else:
                    a = tableWidgetName.item(i, j).text()
                    checkBoxMat[i, j] = a
        print(checkBoxMat)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

