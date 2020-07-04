"""
找出一个正整数所有数字全排列的下一个数（大于当前的数）
"""

def find_nearest_number(array: []):
    """
    找出一个正整数所有数字全排列的下一个数（大于当前的数）
    这里假设正整数各个位数字以及按序保存在数组内
    """
    # 1. 找到逆序区域边界
    num = array[-1]
    border_index = len(array)-1
    for i in range(len(array)-2,-1,-1):
        if array[i]>=num:
            border_index -= 1
            num = array[i]
        else:
            break
    if border_index == 0:
        print("原数字为其全排列最大数字！！！")
        return None
    # 2. 交换逆序区域的前一位和逆序区域中大于它的最小数字
    for j in range(len(array)-1,border_index-1,-1):
        if array[j]>array[border_index-1]:
            tmp = array[j]
            array[j] = array[border_index-1]
            array[border_index-1] = tmp
            break
    # 3. 将逆序区域变为顺序状态
    i = border_index
    j = len(array)-1
    while i<j:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        i += 1
        j -= 1

    return None

if __name__ == "__main__":
    x = [9,8,1,2,3,4,3,7,5,5,4,3]
    print("原数：")
    print(x)
    print("全排列最近邻数（大）：")
    find_nearest_number(x)
    print(x)