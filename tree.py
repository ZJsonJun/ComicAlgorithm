"""
一个二叉树实现
"""

from queue import Queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree(input_list=[]):
    """
    构建二叉树
    input_list: 输入数列
    return: 根节点
    """
    if input_list==None or len(input_list)==0:
        return None
    data = input_list.pop(0)
    if data == None:
        return None
    # 根节点
    Node = TreeNode(data)
    # 左子树
    Node.left = create_binary_tree(input_list)
    # 右子树
    Node.right = create_binary_tree(input_list)
    return Node

def prev_order_traversal(node : TreeNode):
    """
    二叉树的先序遍历： 根节点 --> 左子树  --> 右子树
    """
    # 读取根节点
    if node != None:
        print(node.data)
        # 读取左子树
        prev_order_traversal(node.left)
        # 读取右子树
        prev_order_traversal(node.right)

def last_order_traversal(node : TreeNode):
    """
    二叉树的后序遍历： 左子树 --> 右子树 --> 根节点
    """
    if node != None:
        # 读取左子树
        last_order_traversal(node.left)            
        # 读取右子树
        last_order_traversal(node.right)
        # 读取根节点
        print(node.data)

def mid_porder_traversal(node : TreeNode):
    """
    二叉树中序遍历： 左子树 --> 根节点 --> 右子树
    """
    if node != None:
        # 读取左子树
        mid_porder_traversal(node.left)
        # 读取根节点
        print(node.data)
        # 读取右子树
        mid_porder_traversal(node.right)

def prev_order_traversal_with_stack(node : TreeNode):
    """
    用 stack 实现遍历（回溯）
    """
    stack = []
    while node is not None or len(stack)>0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right

def level_order_traversal(node : TreeNode):
    """
    树的广度优先遍历（层序优先遍历） 队列实现
    """
    queue = Queue()
    if node is not None:
        queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)

class SmallRootPile:
    def __init__(self, data=[]):
        # 拷贝一份
        self.data = data.copy()
        self.len = len(data)
        self.build_pile()

    def up_adjust(self,index):
        """
        将小节点上浮
        """
        if index<0 or index>(self.len-1):
            print("索引越界")
        while(index>0 and self.data[index]<self.data[(index-1)//2]):
            tmp = self.data[index]
            self.data[index]=self.data[(index-1)//2]
            self.data[(index-1)//2] = tmp
            index = (index-1)//2

    def down_adjust(self,index):
        """
        将大节点下沉
        """
        if index<0 and index>(self.len-1):
            print("索引越界")
        while(index*2+1<self.len or index*2+2<self.len):
            # 存在左右子节点
            if index*2+2<self.len:
                swap_index = (index*2+1) if self.data[(index*2+1)]<self.data[(index*2+2)] else (index*2+2)
                if self.data[index]>self.data[swap_index]:
                    tmp = self.data[index]
                    self.data[index] = self.data[swap_index]
                    self.data[swap_index] = tmp
                    index = swap_index
                else:
                    break
            # 只存在左子节点
            else:
                if self.data[index]>self.data[(index*2+1)]:
                    tmp = self.data[index]
                    self.data[index] = self.data[(index*2+1)]
                    self.data[(index*2+1)] = tmp
                    index = index*2+1
                else:
                    break
    
    def insert(self,x):
        """
        向堆插入一个数
        """
        self.len += 1
        self.data.append(x)
        self.up_adjust(self.len-1)  # 调整新加入节点
    
    def pop(self):
        """
        弹出堆顶元素（最小值）
        """
        if self.len == 0:
            print("None element!!!")
        elif self.len == 1:
            self.len -= 1
            return self.data.pop()
        else:
            tmp = self.data[0]
            self.data[0] = self.data.pop()
            self.len -= 1
            self.down_adjust(0)
            return tmp

    def build_pile(self):
        """
        构建堆，依次调整每个非叶子节点
        """
        for i in range((self.len-2)//2,-1,-1):
            self.down_adjust(i)

if __name__ == "__main__":
    input = [3,2,9,None,None,10,None,None,8,None,4]
    root = create_binary_tree(input)
    print("先序遍历")
    prev_order_traversal(root)
    print("后序遍历")
    last_order_traversal(root)
    print("中序遍历")
    mid_porder_traversal(root)
    print("先序遍历")
    prev_order_traversal_with_stack(root)
    print("层序遍历")
    level_order_traversal(root)

    a_list = [9,8,7,6,3,2,1,4,5,3,2,1]
    print("数组调整前：")
    print(a_list)
    smrp = SmallRootPile(a_list)
    print("数组调整后（小根堆）：")
    print(smrp.data)
    print("插入一个大数：")
    print(10001)
    smrp.insert(10001)
    print("插入一个小数：")
    print(5)
    smrp.insert(5)
    print("按从小到大顺序输出：")
    for i in range(smrp.len):
        print(smrp.pop())
