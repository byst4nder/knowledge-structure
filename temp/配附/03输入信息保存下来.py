# 对于lineEdit输入的内容进行读取存储。对于文件读取进行变量加载赋值
# 对于输入进行输入检查，数字必须检查0=130
# 点击新建按钮后，开始保存并进入到下一页中。
#       此处加入时间戳，保存文件名字。一个文件一个人。或者一个文件，多个人。
# 点击查找按钮后，进入查找。如无则暂不查找。查找功能暂不做，没用。
# 设置充填按钮：一键恢复到原始界面。
# 通过InputEdit.ui模拟界面。

# 通过lambda也是一种定义的函数：来实现对重复函数的缩减。取代槽函数。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from 配附.InputEdit import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setupUi(self)
        self.Info_dict = {}
        # 第一种获取方式：
        self.lineEdit.editingFinished.connect(self.save_text)
        # 第二种获取方式：
        # self.lineEdit.textEdited[str].connect(lambda: self.onChange())
    # def onChange(self):
    #     facename = self.lineEdit.text()
    #     print("...！！！！！！", facename)

    def save_text(self):
        name = self.lineEdit.text()
        # print(name)
        self.Info_dict["name1"] = name
        print("dict1:", self.Info_dict)
#   此处最好是有个  装饰器  @ 来记录日志，保存到某个信息：如果出错，就看保存哪个信息出的错。软件很小，暂缓。
#   再次反思，最好是在点击保存或者新建按钮之后，保存对应栏目中的内容，对于内容进行输入检查。
#   新建按钮，触发执行读取输入框或者选择框的内容，以此来保存内容。因此03输入信息保存下来-2触发式保存。



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

