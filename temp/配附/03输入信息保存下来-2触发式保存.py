# 对于一个窗口中的东西，通过点击保存按钮或者新建按钮之后，触发读取保存功能。
# 涉及内容，多复字典赋值。

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from 配附.InputEdit import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setupUi(self)
        # self.Info_dict = {}  # 放入函数中也可以。
        self.pushButton.clicked.connect(self.CreatNewFile)

        # 放在外面就必须加self,就是类内全局变量。
        self.Info_dict = {"baseInfo": {}, "bg_info": {}}

    def CreatNewFile(self):
        # 获取信息，然后赋值，保存到字典。字典放在外面试试。
        # Info_dict = {"baseInfo": {}, "bg_info": {}}
        name = self.lineEdit.text()
        sex = self.comboBox.currentText()
        age = self.lineEdit_2.text()
        print(name, sex, age)
        (self.Info_dict["baseInfo"])["姓名"] = name
        (self.Info_dict["baseInfo"])["性别"] = sex
        (self.Info_dict["baseInfo"])["年龄"] = age
        print("dict1:", self.Info_dict)

#     返回单复选信息：
#     def radioGroupBox_return(self, GroupBoxName, str1):
        # 思路如下:第一种：
        # for temp in radioGroupBoxlist:
        #     if temp.isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()
        #     else:
        #         continue
        # 第二种：
        # if radio[0].isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()
        # elif radio[1].isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()
        # elif radio[2].isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()
        # elif radio[3].isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()

    # def checkGroupBox_return(self, GroupBoxName, str1):
        # (self.Info_dict["bg_info"])[str1] = []
        # for temp in checkGroupBoxlist:
        #     (self.Info_dict["bg_info"])[str1].append(temp.text())
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

