import sys
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.UI_Bone()
        self.left_frame()
        # self.right_frame()

    def UI_Bone(self):
        # 主窗口
        # self.setGeometry(300, 220, 960, 700)
        # self.setFixedSize(960, 700)
        self.setFixedSize(1200, 741)
        # self.resize(960, 700)
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # 左窗口(先构造，后添加，再设置)
        self.left_widget = QWidget()
        self.left_widget.setObjectName("left_widget")
        self.left_layout = QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        # 右窗口(先构造，后添加，再设置)
        self.right_widget = QWidget()
        self.right_widget.setObjectName("right_widget")
        self.right_layout = QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        # 将左右拼接进入到主窗
        self.main_layout.addWidget(self.left_widget, 0, 0, 16, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 16, 10)
        self.setCentralWidget(self.main_widget)

        # 骨框架标签
        self.setWindowTitle('精益项目GUI')
        self.setWindowIcon(QtGui.QIcon('./images/Icon.jpg'))
        # self.show()

    # 左侧菜单栏
    def left_frame(self):
        """先创建，后添加"""
        # 创建左侧按钮
        self.left_TraData_path = QPushButton("训练集")
        # self.left_TraData_path.setFixedSize(15, 15)
        self.left_TraData_path.resize(self.left_TraData_path.sizeHint())

        self.left_ValData_path = QPushButton("验证集")
        # self.left_ValData_path.setFixedSize(15, 15)
        self.left_ValData_path.resize(self.left_ValData_path.sizeHint())

        self.left_TestData_path = QPushButton("测试集")
        # self.left_TestData_path.setFixedSize(15, 15)
        self.left_TestData_path.resize(self.left_TestData_path.sizeHint())

        self.left_TraData_path.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_ValData_path.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_TestData_path.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # 创建左侧标签
        self.left_label_1 = QPushButton("数据集")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QPushButton("操作")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QPushButton("调参")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QPushButton("显示")
        self.left_label_4.setObjectName('left_label')

        # 使用qtawesome这个第三方库来实现按钮中的FontAwesome字体图标的显示。也就是fa
        self.left_button_1 = QPushButton(qtawesome.icon('fa.music', color='yellow'), "训练模型")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QPushButton(qtawesome.icon('fa.sellsy', color='blue'), "测试模型")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QPushButton(qtawesome.icon('fa.film', color='green'), "导出模型")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QPushButton(qtawesome.icon('fa.home', color='red'), "BatchSize")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QPushButton(qtawesome.icon('fa.download', color='white'), "Steps")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QPushButton(qtawesome.icon('fa.heart', color='white'), "Epoch")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QPushButton(qtawesome.icon('fa.comment', color='white'), "执行情况")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QPushButton(qtawesome.icon('fa.star', color='white'), "Loss")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QPushButton(qtawesome.icon('fa.question', color='black'), "Acc")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QPushButton(" ")

        # 将创建的按钮添加到左侧部件的网格布局层中
        self.left_layout.addWidget(self.left_label_1, 0, 0, 1, 3)
        self.left_layout.addWidget(self.left_TraData_path, 1, 1, 1, 1)
        self.left_layout.addWidget(self.left_ValData_path, 2, 1, 1, 1)
        self.left_layout.addWidget(self.left_TestData_path, 3, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_4, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 13, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 14, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 15, 0, 1, 3)

        self.left_widget.setStyleSheet('''
                    QWidget#left_widget{
                        background:gray;
                        border-top:1px solid white;
                        border-bottom:1px solid white;
                        border-left:1px solid white;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;
                    }
                    QPushButton{border:none;color:white;}
                    QPushButton#left_label{
                        border:none;
                        border-bottom:1px solid white;
                        font-size:18px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                ''')

    # 右侧内容模块
    def right_frame(self):
        # 在搜索模块中，有一个文本和一个搜索框，我们通过QLable()部件和QLineEdit()部件来实现，
        # 这两个部件同时包裹在一个网格布局的QWidget()部件，分列第一列和第二列，
        self.right_bar_widget = QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        # 推荐标题使用QLable()来实现；
        self.right_recommend_label = QLabel("今日推荐")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QWidget()  # 推荐封面部件
        self.right_recommend_layout = QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QToolButton()
        self.recommend_button_1.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\r1.jpg'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QToolButton()
        self.recommend_button_2.setText("那首歌")
        self.recommend_button_2.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\r2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QToolButton()
        self.recommend_button_3.setText("伟大的渺小")
        self.recommend_button_3.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\r3.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QToolButton()
        self.recommend_button_4.setText("荣耀征战")
        self.recommend_button_4.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\r4.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QToolButton()
        self.recommend_button_5.setText("猎场合辑")
        self.recommend_button_5.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\r5.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        # 创建音乐列表模块和音乐歌单模块。音乐列表模块和音乐歌单模块都有一个标题和一个小部件来容纳具体的内容。

        # 标题我们都使用QLabel()部件来实现，而音乐列表我们使用网格布局的QWidget()部件下包裹着数个QPushButton()按钮部件来实现，
        # 音乐歌单列表则使用网格布局的QWidget()部件下包裹着数个QToolButton()工具按钮部件来实现。

        self.right_newsong_lable = QLabel("最新歌曲")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QLabel("热门歌单")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_2 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_3 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_4 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_5 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_6 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )

        # 音乐歌单模块的代码
        self.right_playlist_widget = QWidget()  # 播放歌单部件
        self.right_playlist_layout = QGridLayout()  # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QToolButton()
        self.playlist_button_1.setText("无法释怀的整天循环音乐…")
        self.playlist_button_1.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\p1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QToolButton()
        self.playlist_button_2.setText("不需要歌词,也可以打动你的心")
        self.playlist_button_2.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\p2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QToolButton()
        self.playlist_button_3.setText("那些你熟悉又不知道名字…")
        self.playlist_button_3.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\p3.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QToolButton()
        self.playlist_button_4.setText("那些只听前奏就中毒的英文歌")
        self.playlist_button_4.setIcon(QtGui.QIcon('F:\GUI-PyQt5-QSS\p4.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_process_bar = QProgressBar()  # 播放进度部件
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字

        self.right_playconsole_widget = QWidget()  # 播放控制部件
        self.right_playconsole_layout = QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_1 = QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_2 = QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_3 = QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), "")
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.right_widget.setStyleSheet('''
                    QWidget#right_widget{
                        color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-right-radius:10px;
                        border-bottom-right-radius:10px;
                    }
                    QLabel#right_lable{
                        border:none;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.right_newsong_widget.setStyleSheet('''
                    QPushButton{
                        border:none;
                        color:gray;
                        font-size:12px;
                        height:40px;
                        padding-left:5px;
                        padding-right:10px;
                        text-align:left;
                    }
                    QPushButton:hover{
                        color:black;
                        border:1px solid #F3F3F5;
                        border-radius:10px;
                        background:LightGray;
                    }
                ''')

        self.right_process_bar.setStyleSheet('''
                    QProgressBar::chunk {
                        background-color: #F76677;
                    }
                ''')

        self.right_playconsole_widget.setStyleSheet('''
                    QPushButton{
                        border:none;
                    }
                ''')


def main():
    app = QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

