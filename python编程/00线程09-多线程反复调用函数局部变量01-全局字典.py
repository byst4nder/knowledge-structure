# 每个线程处理不同的Student对象，不能共享。
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)


def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)


def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
# 此时多个函数反复调用std,多个线程对std的修改也不同，如果用全局变量共享也无法识别各自线程的值。

# 解决方案一：使用全局字典方式。


global_dict = {}


def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread().name] = std
    do_task_1()
    do_task_2()


def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread().name]
    ...


def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread().name]
    ...
# 消除了std对象在每层函数中的传递问题。每个线程调用的都是自己的值。
# 但是，每个函数获取std的代码有点low。
# 函数与函数之间的调用，就涉及数据的传递。一种方案是考虑用全局变量。费劲。
# 一个线程的赋值，另一个线程的赋值会修改。变量传递混乱。
