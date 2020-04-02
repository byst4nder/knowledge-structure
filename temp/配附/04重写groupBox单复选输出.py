# 通过之前获取children()来解决列表问题，现在通过toggled()状态切换触发来执行读取内容。解决返回值为空问题。
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
    def radioGroupBox_init(self, GroupBoxName):
        for temp in GroupBoxName.children():
            # temp.toggled.connect(lambda: self.readText(GroupBoxName, temp))
            temp.clicked.connect(lambda: self.radioAssign(GroupBoxName))
            # if temp.toggled and temp.isChecked():
            #     self.Info_dict["bg_info"][GroupBoxName.title()] = temp.text()
            #     print(Info_dict)

    def radioAssign(self, GroupBoxName):
        print("GroupBox '%s' 被触发激活..." % GroupBoxName.title())
        for temp in GroupBoxName.children():
            if temp.isChecked():
                self.Info_dict["bg_info"][GroupBoxName.title()] = temp.text()
                print(self.Info_dict)
            else:
                pass

    # 多选返回办法：
    def checkGroupBox_init(self, GroupBoxName):
        # (self.Info_dict["bg_info"])[str1] = []
        # for temp in checkGroupBoxlist:
        #     (self.Info_dict["bg_info"])[str1].append(temp.text())
        checklist = []
        for temp in GroupBoxName.children():
            temp.toggled.connect(lambda: self.checksAssign(GroupBoxName))

    def checksAssign(self, GroupBoxName):
        CheckBox_list = []
        print("GroupBox '%s' 状态被修改..." % GroupBoxName.title())
        for temp in GroupBoxName.children():
            if temp.isChecked():
                CheckBox_list.append(temp.text())
            self.Info_dict["bg_info"][GroupBoxName.title()] = CheckBox_list
        print(self.Info_dict)

    def readGroupBox(self):
        self.radioGroupBox_init(self.groupBox)
        self.checkGroupBox_init(self.groupBox_2)
        # 有多个GroupBox的时候可以直接for遍历来实现。
        # print(self.Info_dict)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

