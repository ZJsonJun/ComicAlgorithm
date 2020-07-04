"""
确定两个有序数组合并后的中位数
"""

def mid_number(arrayA: [], arrayB: []):
    """
    确定两个有序数组合并后的中位数
    """
    # 1. 如果必要，交换数组，确保数组A是短数组，数组B是长数组
    m = len(arrayA)
    n = len(arrayB)
    if m>n:
        arrayA, arrayB, m, n = arrayB, arrayA, n, m
    # 初始化i的搜索区域
    start, end, half_len = 0, m, (m+n+1)//2
    while start<=end:
        i = (start+end)//2
        j = half_len - i
        if i<m and arrayB[j-1]>arrayA[i]:
            # i 偏小了，右移
            start = i+1
        elif i>0 and arrayA[i-1]>arrayB[j]:
            # i 偏大了，左移
            end = i-1
        else:
            # i 刚合适，或i已经到达数组边界
            if i == 0:
                max_left = arrayB[j-1]
            elif j == 0:
                max_left = arrayA[i-1]
            else:
                max_left = max(arrayA[i-1],arrayB[j-1])
            if (m+n)&1 == 1:
                # 如果合并和数组长度为奇数，则中位数是左半部分的最大值
                return max_left
            if i == m:
                min_right = arrayB[j]
            elif j == n:
                min_right = arrayA[i]
            else:
                min_right = min(arrayA[i],arrayB[j])
            # 如果合并数组长度为偶数，则中位数为左侧最大值与右侧最小值取平均
            return (max_left+min_right)/2.0

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    b = [3,5,6,8,9,10,12,14]
    print(mid_number(a,b))