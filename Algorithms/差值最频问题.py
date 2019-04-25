# 算法题目：
# 从1到50这五十个数字中，随机取两个数，然后将两数差值的绝对值放回，两数丢弃。直到只剩最后一个数。差值出现最多的数是几？


import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

appear = []
for j in range(2**16):
    # for j in range(2048):
    num = list(np.arange(1, 33, 1))
    L = []
    for i in range(31):

        random.shuffle(num)
        rand1 = random.randint(0, len(num)-1)
        num1 = num[rand1]
        del num[rand1]
        rand2 = random.randint(0, len(num)-1)
        num2 = num[rand2]
        del num[rand2]
        result = abs(num1 - num2)
        num.append(result)

        L.append(result)

    c = np.array(L)
    d = np.argmax(np.bincount(c))

    appear.append(d)


c1 = np.array(appear)
d0 = np.bincount(c1)
pinshu = Counter(appear)
print(pinshu)
d1 = np.argmax(d0)
print(d1)
# sor = sorted(pinshu.items(), key=lambda x: x[1], reverse=True)
sor = sorted(pinshu.items(), key=lambda x: x[0], reverse=False)
print(sor)

print(type(sor))
# random.choice(L) 也可以实现选数。
# plt.plot(pinshu[:][0], pinshu[:][1], "g:s")
bins = len(pinshu)
plt.hist(appear, bins=bins, edgecolor="None", facecolor="red")
plt.show()
