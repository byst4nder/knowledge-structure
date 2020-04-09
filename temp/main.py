# -*- coding: utf-8 -*-
import sys
import time
from mainLogic import MyMainWindow
from PyQt5.QtWidgets import QApplication

sys.setrecursionlimit(1000000)
log_file = open('logTest.txt', 'a+', buffering=1, encoding="utf-8")
sys.stdout = log_file
sys.stderr = log_file
sys.stdin = log_file
print(time.strftime("%Y-%m-%d %H:%M:%S------", time.localtime()), "软件开启，日志工作中。。。。。 ***************")


def main():
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
