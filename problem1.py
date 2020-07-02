"""
判断单向链表是否有环
"""

class Node:
    """
    节点类
    """
    def __init__(self,data):
        self.data = data
        self.next = None

def is_circle(head: Node):
    """
    判断单向链表是否有环
    解题思路：追及问题，快慢指针
    head: 链表的头节点
    """
    p1 = head
    p2 = head
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1==p2:
            return True
    return False

def circle_length(head: Node):
    """
    若单向链表有环，计算环的长度（环上节点数）
    """
    p1 = head
    p2 = head
    len = -1
    # 首次相遇
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1==p2:
            len = 0     # 标记计数开始
            break
    # 速度差：v2-v1=1, 当再次相遇时，p2比p1正好多走一个环的长度
    # (v2-v1)*step = circle_len
    while True:
        p1 = p1.next
        p2 = p2.next.next
        len += 1
        if p1==p2:
            break
    return len

def circle_joint(head: Node):
    """
    若单向链表有环，定位入环节点
    """
    p1 = head
    p2 = head
    # 首次相遇
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1==p2:
            break
    # D = (N-1)(S1+S2)+S2
    p1 = head   # p1重新放到head位置
    while True:
        p1 = p1.next
        p2 = p2.next
        if p1==p2:
            break
    return p1

if __name__ == "__main__":
    # 创建一个有环的单向链表
    node_list = []
    for i in range(10):
        node_list.append(Node(i))
    for j in range(9):
        node_list[j].next = node_list[j+1]
    node_list[9].next = node_list[3]
    # 判断是否有环
    head = node_list[0]
    is_circled = is_circle(head)
    print(is_circled)
    if is_circled:
        print("环的长度：")
        print(circle_length(head))
    if is_circled:
        print("入环节点：")
        print(circle_joint(head).data)