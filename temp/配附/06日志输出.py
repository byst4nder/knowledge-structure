# -*- coding: utf-8 -*-

import sys
# if not hasattr(sys, 'argv'):
#     sys.argv = ['06日志输出.py']
log_file = open('log_TEST.txt', 'w+', buffering=1, encoding="utf-8")
sys.stdout = log_file
sys.stderr = log_file
sys.stdin = log_file

print("启动测试日志输出方式。打印print内容。。。")
a = 0
b = 1/a
print("B", b)
