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
    """
    if input_list==None or len(input_list)==0:
        return None
    data = input_list.pop(0)
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




if __name__ == "__main__":
    input = [2,3,4,5,6,9,7]
    tree_head = create_binary_tree(input)
    prev_order_traversal(tree_head)
