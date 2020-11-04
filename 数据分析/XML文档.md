XML文档



XML文档——**树结构**：

> - 1、XML文档必须包涵 **根元素**。该元素是所有其他元素的父元素。
>
> - 2、所有的元素**都可以**有子元素。
> - 3、最外层的为**根**。必须有根元素。
> - 4、所有元素都可以有**文本(内容)**和**属性**。
> - 5、HTML中可以省略关闭标签；但是XML**必须有关闭标签**。
> - 6、XML的属性中的**值(value)**必须加**引号**。



XML **元素**指的是从（且包括）**开始标签**直到（且包括）**结束标签**的部分。



注释写法：

```XML
<!-- This is a comment -->
```


声明写法：
```xml
<?xml version="1.0" encoding="utf-8"?>
```





| 实体引用 | 显示符号 | 含义           |
| -------- | -------- | -------------- |
| \&lt;    | <        | less than      |
| \&gt;    | >        | greater than   |
| \&amp;   | &        | ampersand      |
| \&apos   | '        | apostrophe     |
| \&quot   | "        | quotation mark |





```python
from xml.dom.minidom import parse


domTree = parse(xmlName)
# 文档对象：根元素
# 一次性读入，文档过大容易导致内存溢出，同时时间效率。
rootNode = domTree.documentElement
print(rootNode.nodeName)
# 标签属性值
print(rootNode.getAttribute("name"))

# 得到子元素对象,NodeList
subElementObj = rootNode.getElementsByTagName("filename")
print(subElementObj[0].nodeName)
print(type(subElementObj))
print(len(subElementObj))
# 显示标签对之间的数据，文本/内容。
print(subElementObj[0].firstChild.data)

NGID = rootNode.getElementsByTagName("name")
print(len(NGID))
print(NGID[0].firstChild.data)
```

获取标签用getElementsByTagName("标签名字")

获取属性用getAttribute(“属性名字”)

获取内容用subElementObj[0].firstChild.data


https://www.py.cn/jishu/jichu/13306.html