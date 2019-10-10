# 参考文献：https://blog.csdn.net/s740556472/article/details/80928849
# 参考文献：https://blog.csdn.net/Beyond_F4/article/details/80590082

# S1:动态生成变量名：locals函数

# 生成变量并赋值：
for i in range(3):
    locals()["a"+str(i)] = i

print(a1)

# 常用做法：
listTemp = ["aa", "bb", "cc", "dd"]
for i, s in enumerate(listTemp):
    locals()["var"+str(i)] = s
print(var0, var1, var2, var3)

# 再拓展：
listTemp2 = locals()
for i in range(3):
    listTemp2["varT"+str(i)] = i
print(listTemp2["varT1"])
print(type(listTemp2))
print(listTemp2["__file__"])   # 输出了运行文件的文件名，
print(listTemp2["__name__"])   # 输出了运行的函数名。
print(listTemp2.keys())
print(listTemp2)  # 文件名，包名，函数名，变量名，都可以再其中进行操作。


# ####################################################################################################################
# S2:提取变量名：
import inspect

test_str = "12rtar"


def get_var_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    # return [var_name for var_name, var_val in callers_local_vars if var_val is variable]
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable][0]


print(get_var_name(test_str))
print(type(get_var_name(test_str)))
print(type(eval(get_var_name(test_str))))

print("+++++++++++++++++++++++++++++++++++++")
# S3：从变量名，获取变量值。
import sys

test_str2 = "12517gfj"


def get_var_name2(varname):
    return [sys._getframe().f_back.f_locals[varname]][0]


print(get_var_name2("test_str2"))


