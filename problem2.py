"""
最小栈问题
实现一个栈，它有三个方法：
1. 出栈
2. 入栈
3. 取当前栈最小值
N.B. 要求三个方法的时间复杂度都为O(1)
"""

class stack:
    def __init__(self):
        self.data = []      # 当前栈
        self.copy = []      # 保存历史最小值的栈
        self.min = None
    
    def push(self,num: int):
        # 初始化，栈空
        if len(self.data) == 0:
            self.min = num
            self.data.append(num)
            self.copy.append(num)
        # 入栈
        else:
            self.data.append(num)
            # 如果入栈的值比当前最小值还小
            # 其还要入copy栈
            if num <= self.min:
                self.min = num
                self.copy.append(num)

    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            tmp = self.data.pop()
            # 如果弹出的值是最小值，那么copy栈也要跟着弹出栈顶元素（当前最小值）
            # 之后更新当前最小值
            if tmp == self.min:
                self.copy.pop()
                self.min = self.copy[-1]    # 更新当前最小值
        return tmp

    def get_min(self):
        if len(self.data) == 0:
            return None
        return self.copy[-1]



if __name__ == "__main__":
    s1 = stack()
    for i in range(10,0,-1):
        s1.push(i)
    for j in range(20,-1,-1):
        s1.push(j)
    print("当前栈中最小值：")
    print(s1.get_min())
    print("出栈25个元素：")
    for _ in range(25):
        print(s1.pop())
    print("当前栈中最小值：")
    print(s1.get_min())