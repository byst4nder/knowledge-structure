树与树算法：

	·节点的度：一个节点含有的子树的个数称为该节点的度；
	·树的度：一棵树中，最大的节点的度称为树的度；
	树的种类：
		无序树：树中任意节点的子节点之间没有顺序关系，这种树称为无序树，也称为自由树；
		有序树：树中任意节点的子节点之间有顺序关系，这种树称为有序树；
			二叉树：每个节点最多含有两个子树的树称为二叉树；
				完全二叉树：对于一颗二叉树，假设其深度为d(d>1)。除了第d层外，其它各层的节点数目均已达最大值，且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树，其中满二叉树的定义是所有叶节点都在最底层的完全二叉树;
				平衡二叉树（AVL树）：当且仅当任何节点的两棵子树的高度差不大于1的二叉树；
				排序二叉树（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）；
			霍夫曼树（用于信息编码）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；
			B树：一种对读写操作进行优化的自平衡的二叉查找树，能够保持数据有序，拥有多余两个子树。

	树的存储：
		顺序存储：
			将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，但因所占空间比较大，是非主流二叉树。二叉树通常以链式存储。
		链式存储：
			可以存储，缺陷：指针域指针个数不定。
			解决方案：把多叉树，转成二叉树。


	树的应用场景：
		1.xml，html等，那么编写这些东西的解析器的时候，不可避免用到树。
		2.路由协议就是使用了树的算法。
		3.mysql数据库索引。
		4.文件系统的目录结构。
		5.所以很多经典的AI算法其实都是树搜索，此外机器学习中的decision tree也是树结构。
			k近邻法的实现：kd树是二叉树，为了提高K近邻搜索的效率。本质是二叉排序树。

二叉树：
	二叉树是每个节点最多有两个子树的树结构。通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）

二叉树节点表示以及树的创建。

	# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
	class Node(object):
	    '''节点类'''
	    def __init__(self, elem=-1, lchild=None, rchild=None):
	        self.elem = elem
	        self.lchild = lchild
	        self.rchild = rchild

	# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
	class Tree(object):
	    '''树类'''
	    def __init__(self):
	        self.root = None

	    def add(self,elem):
	        '''为树添加节点'''
	        node = Node(elem)
	        # 如果树是空的，则对根节点赋值：
	        if self.root == None:
	            self.root = node
	            return
	        queue = [self.root]  # 队列可以用列表来表示。
	        # 对已有的节点进行层次遍历
	        while queue:
	            # 弹出队列的第一个元素：查看当前节点左右位置是否有左右孩子，分别赋值。
	            cur_node = queue.pop(0)  # 对头开始取数。
	            if cur_node.lchild ==None:
	                cur_node.lchild = node
	                return
	            elif cur_node.rchild == None:
	                cur_node.rchild = node
	                return
	            else:
	                # 如果左右子树都不为空，加入队列继续判断.
	                queue.append(cur_node.lchild)
	                queue.append(cur_node.rchild)

	    def breadth_travel(self):
	        '''广度遍历'''
	        if self.root is None:
	            return
	        queue = [self.root]
	        while queue:
	            cur_node = queue.pop(0)
	            print(cur_node.elem, end=' ')
	            if cur_node.lchild is not None:
	                queue.append(cur_node.lchild)
	            if cur_node.rchild is not None:
	                queue.append(cur_node.rchild)

	    def preorder(self, node):
	        '''先序遍历'''
	        # 递归方法都特别简短。
	        if node is None:
	            return
	        print(node.elem, end=' ')
	        self.preorder(node.lchild)
	        self.preorder(node.rchild)

	    def inorder(self, node):
	        '''中序遍历'''
	        # 递归方法都特别简短。
	        if node is None:
	            return
	        self.inorder(node.lchild)
	        print(node.elem, end=' ')
	        self.inorder(node.rchild)

	    def postorder(self, node):
	        '''后序遍历'''
	        # 递归方法都特别简短。
	        if node is None:
	            return
	        self.postorder(node.lchild)
	        self.postorder(node.rchild)
	        print(node.elem, end=' ')


	if __name__ == '__main__':
	    tree = Tree()
	    tree.add(0)
	    tree.add(1)
	    tree.add(2)
	    tree.add(3)
	    tree.add(4)
	    tree.add(5)
	    tree.add(6)
	    tree.add(7)
	    tree.add(8)
	    tree.add(9)
	    tree.breadth_travel()
	    print('\n')
	    tree.preorder(tree.root)
	    print('\n')
	    tree.inorder(tree.root)
	    print('\n')
	    tree.postorder(tree.root)



深度遍历：
	三种深度遍历方式：由根的选取时间来定。
		先序遍历：根左右：根节点->左子树->右子树
		中序遍历：左根右：左子树->根节点->右子树
		后序遍历：左右根：左子树->右子树->根节点

给一个序列如何将图画出：
	必须要有一个中序，先后给一个即可。求另一个。