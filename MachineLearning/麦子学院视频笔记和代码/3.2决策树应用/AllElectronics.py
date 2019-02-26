from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
allElectronicsData = open(r'./AllElectronics.csv', 'r+')  # 加载打开csv文件。原文rb，
reader = csv.reader(allElectronicsData)  # 读取csv文件。
headers = next(reader)  # 第一行
# 此处原文为：headers = reader.next() python3不可用。

# print(headers)

# 一般我们加载数据要初始化连个列表：一个是特征的，一个是分类标签的。
featureList = []
labelList = []  # 列表将字典里面的特征保存下来。python自带模块可以实现将字典格式的数据转化为1000100101基因编码形式。

for row in reader:   # 按列取值。
    labelList.append(row[len(row)-1])   # 最后一列为输出结果列。

    # 定义个词典保存特征取值：
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

# print(featureList)

# Vectorize features  实例化、特征向量化
vec = DictVectorizer()  # 该方法可用pandas中的get_dummies实现（同样可以实现one-hot编码）。
dummyX = vec.fit_transform(featureList) .toarray()

print("dummyX: " + str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

# vectorize class labels 标签也完成实例化：
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))

# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)   # 直接利用sklearn下面的tree中类来建立决策树模型
print("clf: " + str(clf))


# Visualize model  将决策树打印出来。
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# Graphviz这个工具可以将.dot文件画出来，转换成pdf保存下来。
# 点击下面Terminal输入：dot allE[Tab] _T pdf -o output.pdf
# 或者dot dot allE[Tab] _T png -o output2.txt
# https://www.cnblogs.com/shuodehaoa/p/8667045.html

# 应用这个决策树来分类：
oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

# 修改某个值，新样本。
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict([newRowX, ])
print("predictedY: " + str(predictedY))
if predictedY == 1:
    print("预测此人将购买电脑！")
if predictedY == 0:
    print('预测此人不会购买电脑！')


