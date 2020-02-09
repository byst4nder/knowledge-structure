import csv

print("操作提示:")
print("0:写\n1:读")
while True:
    a = int(input("请输入要进行的操作:"))

    datas = [['name', 'age'],
             ['Bob', 14],
             ['Tom', 23],
            ['Jerry', '18']]
    if a == 0:
        with open("./example.cfg", "w", newline="") as f:
            # fieldnames = ["___Item_name___", "parameters"]
            writer = csv.writer(f, dialect="excel")       # 此处用excel格式
            for row in datas:
                writer.writerow(row)
            print("2")
            # writer.writerows(datas)

    if a == 1:
        with open("./example.csv") as f:
            reader = csv.reader(f)
            print(list(reader))
            print(list(reader))

            print(list(reader)[1][1])
            a = list(reader)[1][1]
            print(a)
            print(type(a))


# IndexError: list index out of range
# 对错误的理解：
# with open() as f:这种打开方式，是生成器的方式，只有一次调用机会，所以必须保存下来，一旦别人调用过，那么将无法再次调用。
# 生成器，一旦调用，就释放，再也无法重新使用。
# 因此将用一个列表将结果保存下来。

