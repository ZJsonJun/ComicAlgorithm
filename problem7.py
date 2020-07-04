"""
给出一个整数，从该整数中去掉k个数字，
要求剩下的数字形成的新整数尽可能小。
"""

def smallest_removeKdigits(array: [], k: int):
    """
    给出一个整数，从该整数中去掉k个数字，
    要求剩下的数字形成的新整数尽可能小。
    """
    n = len(array)
    array_new = []    # 用于保存新整数
    index = 0
    # 1. 从左到右（高位到低位）删除数字
    # 如果该位数字大于其相邻低位数字，则删除
    # 让小数字成为新整数的高位（原则）
    while index<n-1:
        if k == 0:
            break
        if array[index]>array[index+1]:
            array[index] = None
            k -= 1
        index += 1
    # 2. 将剩余数字按序填充到新数组
    for num in array:
        if num is not None:
            array_new.append(num)
    # 3. 第一步可能找不齐k个满足条件的数字
    # 这时候需要补齐k个数字，因为剩下的数字都是顺序了
    # 所以从右到左删除数字，补齐k个
    for _ in range(k):
        array_new.pop()
    # 如果所有数字都被删除了，则返回0
    if len(array_new) == 0:
        return [0]
    return array_new

if __name__ == "__main__":
    # int_num = [5,4,1,2,7,0,9,3,6]
    int_num = [1,1,1,1,1,1,1,1,1,1]
    print("原整数：")
    print(int_num)
    new_num = smallest_removeKdigits(int_num, 10)
    print("新整数：")
    print(new_num)