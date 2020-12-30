# 方法一：for...else的方法。可以实现这个功能。
for i in range(5):
    for j in range(5):
        if i + j == 5:
            print(i, j)
            break
    else:
        continue
    break


# 方法二：函数return方法。
def sum5():
    for i in range(5):
        for j in range(5):
            if i + j == 5:
                print(i, j)
                return

sum5()

# 方法三：标记变量
flag = True
for i in range(5):
    for j in range(5):
        if i + j == 5:
            print(i, j)
            flag = False
            break
        
    if not flag:
        break
    






