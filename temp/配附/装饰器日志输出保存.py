# 加入时间戳，保存关键数据存储和关键步骤，打印中间状态。
# 暂时软件不大，暂时不加，但是需要整理方法，后续在慢慢添加。
import time, datetime

time = time.localtime()
print(time)

data = datetime.datetime.now()
print(data.strftime("%Y-%m-%d-%H%M%S"))

fileName = data.strftime("%Y-%m-%d-%H%M%S") + ".json"
print(fileName)