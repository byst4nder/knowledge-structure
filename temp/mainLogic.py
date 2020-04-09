# -*- coding: utf-8 -*-

import os
import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox
from mainUI import Ui_MainWindow
import json

# Version1.01 解决一个新建一个文件保存的问题。
# 后续需要更新设置输入格式限制的问题，以及部分美工。


sys.setrecursionlimit(1000000)


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 定义数据结构：字典json形式。
        self.Info_dict = {"baseInfo": {}, "bg_info": {}, "HHIE-S": {}, "Estimate": {}}
        self.myInit()
        self.file = 0

    def myInit(self):
        # 左侧插件控制右侧主窗显示：
        self.Btn1_BaseInfo.clicked.connect(lambda: self.stack_display(0))
        self.Btn2_Backgroud.clicked.connect(lambda: self.stack_display(1))
        self.Btn3_HHIES.clicked.connect(lambda: self.stack_display(2))
        self.Btn4_Estimate.clicked.connect(lambda: self.stack_display(3))

        # Page1内容编辑：
        self.Btn_New.clicked.connect(self.CreatNewFile)
        self.Btn_Reset.clicked.connect(self.ResetUI)

        # Page2内容编辑
        self.readPage2GroupBox()
        self.Btn_Save2.clicked.connect(lambda: self.stack_display(2))

        # Page3内容编辑：
        self.readPage3GroupBox()
        self.Btn_Save3.clicked.connect(lambda: self.stack_display(3))

        # Page4内容编辑：
        self.saveTable()
        self.Btn_Save4.clicked.connect(self.closeFile)
        self.Btn_Save4.clicked.connect(lambda: self.stack_display(0))
    # ===============================================主页面切换函数==================================

    def stack_display(self, n):
        self.stackedWidget.setCurrentIndex(n)

    # =======================Page1页面函数===========================================================
    def CreatNewFile(self):
        name = self.lineEdit_1.text()
        sex = self.comboBox.currentText()
        age = self.lineEdit_2.text()
        # print(name, sex, age)
        (self.Info_dict["baseInfo"])["姓名"] = name
        (self.Info_dict["baseInfo"])["性别"] = sex
        (self.Info_dict["baseInfo"])["年龄"] = age
        # print("dict1:", self.Info_dict)

        date = datetime.datetime.now()
        fileName = date.strftime("%Y-%m-%d-%H%M%S") + ".json"
        filePath = "./data/"
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        path = os.path.join(filePath, fileName)
        self.file = open(path, "wt", encoding="utf-8")
        json.dump(self.Info_dict, self.file, ensure_ascii=False, indent=4)
        # 点击新建按钮后将输入保存下来，然后跳转到第二页。
        self.stackedWidget.setCurrentIndex(1)

    # ==========================Page2页面函数==========================================================
    def readPage2GroupBox(self):
        list_groupBoxPage2 = self.groupBox_BackGround.children()
        # print(list_groupBoxPage2[0].title())
        for temp in list_groupBoxPage2[:-2]:
            self.radioGroupBox_init1(temp)
            # print(temp.title())
        for temp in list_groupBoxPage2[-2:]:
            self.checkGroupBox_init(temp)

    # ------单选函数部分-------
    def radioGroupBox_init1(self, GroupBoxName):
        for temp in GroupBoxName.children():
            temp.clicked.connect(lambda: self.radioAssign1(GroupBoxName))

    def radioAssign1(self, GroupBoxName):
        print("GroupBox '%s' 被触发激活..." % GroupBoxName.title())
        for temp in GroupBoxName.children():
            if temp.isChecked():
                self.Info_dict["bg_info"][GroupBoxName.title()] = temp.text()
                print(self.Info_dict)

    # ------------------------多选返回办法：--------------------------------
    def checkGroupBox_init(self, GroupBoxName):
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

    # =======================================Page3*********************************************
    def readPage3GroupBox(self):
        list_groupBoxPage3 = [temp for temp in self.groupBox_HHIE.children() if type(temp) == QGroupBox]
        # print(list_groupBoxPage3.title())
        for temp in list_groupBoxPage3:
            self.radioGroupBox_init2(temp)

    # ------单选函数部分-------
    def radioGroupBox_init2(self, GroupBoxName):
        for temp in GroupBoxName.children():
            temp.clicked.connect(lambda: self.radioAssign2(GroupBoxName))

    def radioAssign2(self, GroupBoxName):
        print("GroupBox '%s' 被触发激活..." % GroupBoxName.title())
        for temp in GroupBoxName.children():
            if temp.isChecked():
                self.Info_dict["HHIE-S"][GroupBoxName.title()] = temp.text()
                print(self.Info_dict)

    # ========================================Page4************************************************
    def saveTable(self):
        self.Btn_Save4_1.clicked.connect(lambda: self.readTable(self.tableWidget4_1))
        self.Btn_Save4_2.clicked.connect(lambda: self.readTable(self.tableWidget4_2))
        self.Btn_Save4_3.clicked.connect(lambda: self.readTable(self.tableWidget4_3))

    def readTable(self, tableWidgetName):
        print("保存按钮被点击")
        print(tableWidgetName.parent().title())
        checkBoxMat = []
        # print(checkBoxMat)
        for i in range(tableWidgetName.rowCount()):
            for j in range(tableWidgetName.columnCount()):
                if tableWidgetName.item(i, j) is None:
                    checkBoxMat.append(0)
                else:
                    a = tableWidgetName.item(i, j).text()
                    checkBoxMat.append(float(a))
        self.Info_dict["Estimate"][tableWidgetName.parent().title()] = checkBoxMat
        print(self.Info_dict)

    # ====================================保存输出文件========================================
    def saveFile(self):
        json.dump(self.Info_dict, self.file, ensure_ascii=False, indent=4)

    def closeFile(self):
        self.file.close()

    def ResetUI(self):
        self.setupUi(self)
        # 定义数据结构：字典json形式。
        self.Info_dict = {"baseInfo": {}, "bg_info": {}, "HHIE-S": {}, "Estimate": {}}
        self.myInit()
        self.file = 0


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWin = MyMainWindow()
#     myWin.show()
#     sys.exit(app.exec_())
