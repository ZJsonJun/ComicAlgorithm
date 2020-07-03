"""
用栈实现队列
"""

class StackQueue:
    """
    维护两个栈，一个用于出队，一个用于入队
    """
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self,x):
        """
        将元素压入 stack_in
        """
        self.stack_in.append(x)

    def pop(self):
        """
        元素出栈是从stack_out栈弹出栈顶元素的
        如果stack_out为空，需要将当前stack_in元素一一弹出压入stack_out
        """
        # 出队列栈为空
        if len(self.stack_out) == 0:
            # 入队列栈也为空
            if len(self.stack_in) == 0:
                return None
            else:   # 将入队列栈元素压入出队列栈
                for _ in range(len(self.stack_in)):
                    self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        else:
            return self.stack_out.pop()

if __name__ == "__main__":
    q1 = StackQueue()
    for i in range(10):
        q1.push(i)
    for _ in range(5):
        print(q1.pop())
    for i in range(3):
        q1.push(i)
    for _ in range(9):
        print(q1.pop())