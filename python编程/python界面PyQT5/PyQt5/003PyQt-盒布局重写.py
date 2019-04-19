import sys
import qtawesome
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication, QEvent
# from PyQt5.QtWidgets import (QAction, qApp, QMainWindow, QWidget,
#                              QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMenu, QLabel，
#                              QHBoxLayout, QVBoxLayout,)
from PyQt5.QtWidgets import *


# class Example(QWidget):

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # self.setGeometry(300, 220, 960, 700)
        self.resize(960, 700)

        self.center()
        self.buttonSet()
        self.ActionSet()
        self.barSet()
        self.menuSet()
        self.labelSet()
        myWidget = QWidget()
        myWidget.setLayout(self.vbox)
        self.setCentralWidget(myWidget)

        # self.setLayout(self.vbox)

        self.setWindowTitle('精益项目GUI')
        self.setWindowIcon(QIcon('./images/Icon.jpg'))
        self.show()

    def closeEvent(self, event):   #

        reply = QMessageBox.question(self, 'QuitMessage',
                                     "Are you sure to quit?\n（提示：若无模型训练，可退出。\n请勿在训练过程中退出！！）",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                                     )

        # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否者就忽略关闭事件。
        if reply == QMessageBox.Yes:
            # QCoreApplication.instance().quit()
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonSet(self):
        QToolTip.setFont(QFont('SansSerif', 10))  # 静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        btn_train = QPushButton('Train', self)  # 创建一个按钮
        btn_train.setToolTip('Start to <b>Train</b> a model!')  # 创建一个按钮提示框，当鼠标悬浮于按钮时，提示内容。
        btn_train.resize(btn_train.sizeHint())
        # btn_train.move(110, 150)

        btn_test = QPushButton('Test', self)  # 创建一个按钮
        btn_test.setToolTip('Start to <b>Test</b> a model!')  # 创建一个按钮提示框，当鼠标悬浮于按钮时，提示内容。
        btn_test.resize(btn_test.sizeHint())
        # btn_test.move(110, 200)

        btn_quit = QPushButton('Quit', self)
        btn_quit.setToolTip('Push to <b>Exit</b>!')  # 创建一个按钮提示框，当鼠标悬浮于按钮时，提示内容。
        btn_quit.clicked.connect(QCoreApplication.instance().quit)  # 可直接退出
        # btn_quit.clicked.connect(self.closeEvent)
        # btn_quit.clicked.connect(self.event)
        btn_quit.resize(btn_quit.sizeHint())
        # btn_quit.move(800, 600)

        self.vbox.addStretch(1)
        self.vbox.addWidget(btn_train)
        self.vbox.addStretch(1)
        self.vbox.addWidget(btn_test)
        self.vbox.addStretch(8)
        self.hbox.addWidget(btn_quit)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)

    def ActionSet(self):
        self.exitAct = QAction(QIcon('./images/exit.png'), '&Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

        self.viewStatAct = QAction('View statusbar', self, checkable=True)
        self.viewStatAct.setStatusTip('View statusbar')
        self.viewStatAct.setChecked(True)
        self.viewStatAct.triggered.connect(self.toggleMenu)

    def barSet(self):

        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')
        self.statusBar()
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(self.exitAct)

    def menuSet(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        impMenu = QMenu("Input", self)
        impAct = QAction("Import file", self)
        impMenu.addAction(impAct)
        DocAct = QAction("Documentation", self)
        aboutAct = QAction("About", self)

        newAct = QAction("New", self)
        # 上面构造，下面添加。
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(self.exitAct)
        toolsMenu = menubar.addMenu("&Tools")
        viewMenu = menubar.addMenu('View')
        helpMenu = menubar.addMenu("&Help")
        helpMenu.addAction(DocAct)
        helpMenu.addAction(aboutAct)
        viewMenu.addAction(self.viewStatAct)

    def labelSet(self):
        short_lbl = QLabel("此处加个标签：\n <b>以观其效</b> !!", self)
        short_lbl.move(300, 500)

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):

           cmenu = QMenu(self)

           TrainAct = cmenu.addAction("&Train")
           TestAct = cmenu.addAction("Test")
           quitAct = cmenu.addAction("&Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))

           if action == quitAct:
               qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# ERROR :
#   QWidget::setLayout: Attempting to set QLayout "" on Example "", which alread  has a layout。
#   继承QMainWindow类条件下：已有一个Layout存在：

# 在Qt的主窗口(MainWindow)中使用setLayout()函数时，运行时即会报如题所示的错误，
# MainWindow主框架已经有了一个Layout了，Layout包括了菜单栏、工具栏、停驻窗口区、中心窗口区、底部状态栏五部分，

# 如果还要再使用一个Layout来布局，可以新建一个窗口，在新建的窗口中使用Layout,
# 然后在使用SetCentralWidget()将新建的窗口设成主窗口的Central Widget

# 代码：
# myWidget = QWidget()
# myWidget.setLayout(self.vbox)
# self.setCentralWidget(myWidget)
