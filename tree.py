"""
一个二叉树实现
"""

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

if __name__ == "__main__":
    input = [3,2,9,None,None,10,None,None,8,None,4]
    root = create_binary_tree(input)
    print("先序遍历")
    prev_order_traversal(root)
    print("后序遍历")
    last_order_traversal(root)
    print("中序遍历")
    mid_porder_traversal(root)