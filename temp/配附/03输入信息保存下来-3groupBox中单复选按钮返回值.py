# 通过读取groupBox中的子控件。获取子选项按钮内容，通过对状态的判断。来返回groupBox单复选按钮返回值。
# 核心代码是：
# for checkbox in groupbox.findChildren(QtGui.QCheckBox):
#     print("'%s: %s' % (checkbox.text(), checkbox.isChecked()))
# 要获取组合框,该复选框属于：groupbox = checkbox.parent()
# 通过父与子之间的继承，获取彼此。
# 纠正：findChildren()只能返回一个值。但是children(),可以将所有值返回。

# 参考文献：
# 1、https://blog.csdn.net/zzzzzz__/article/details/100224383
# 2、http://ddrv.cn/a/355430    如何获取PyQt中QGroupbox中存在的Qcheckbox的状态   ===>>>>算法网。

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from 配附.InputEdit import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Info_dict = {"baseInfo": {}, "bg_info": {}}
        self.readGroupBox()   # 如果加self，会报错：takes 1 positional argument but 2 were given

#         ================从此处开始添加新内容，获取子按钮尝试======================
        list_raidoBtn = self.groupBox.children()
        list_checkBtn = self.groupBox_2.children()
        # print(list_btn.text())
        for radioBtni in list_raidoBtn:
            print('%s: %s' % (radioBtni.text(), radioBtni.isChecked()))
        for checkBtni in list_checkBtn:
            print('%s: %s' % (checkBtni.text(), checkBtni.isChecked()))

#     返回单复选信息：
    def radioGroupBox_return(self, GroupBoxName):
        # 思路逻辑如下:第一种：GroupBoxName.children(radioButton)
        # for temp in radioGroupBoxlist:
        #     if temp.isChecked():
        #         (self.Info_dict["bg_info"])[str1] = temp.text()
        #     else:
        #         continue
        for temp in GroupBoxName.children():
            if temp.isChecked():
                return temp.text()

    def readGroupBox(self):
        self.Info_dict["bg_info"]["归属地"] = self.radioGroupBox_return(self.groupBox)
        self.Info_dict["bg_info"]["爱好"] = self.checkGroupBox_return(self.groupBox_2)
        print(self.Info_dict)

        # 此处需要修改为：temp.toggled.connect(radioGroupBox_return)：状态切换了，就需要触发信号。
        # 设置触发激活功能后再读取text()。详细见pdf教程。目前的方法无法读取选项。
        # ==================================重写一个==========================================

    def checkGroupBox_return(self, GroupBoxName):
        # (self.Info_dict["bg_info"])[str1] = []
        # for temp in checkGroupBoxlist:
        #     (self.Info_dict["bg_info"])[str1].append(temp.text())
        checklist = []
        for temp in GroupBoxName.children():
            if temp.isChecked():
                checklist.append(temp.text())
        return checklist


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

