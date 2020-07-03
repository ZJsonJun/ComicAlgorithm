"""
无序数组排序后的最大相邻差
"""

class Bucket:
    """
    只记录落在该同区间范围内的最大值和最小值
    """
    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')

def get_maxGap(array: []):
    """
    得到无序数组排序后的最大相邻差（并不实际排序）
    """
    n = len(array)
    bucket_list = [Bucket() for i in range(n)]
    offset = min(array)
    interval = (max(array)-offset)/(n-1)
    # 遍历原始数组，将元素放置到合适的桶内
    # 实际上只记录该桶区间内的最大值和最小值
    # 注意桶区间，左闭右开
    for tmp in array:
        index = int((tmp-offset)/interval)
        if tmp>bucket_list[index].max:
            bucket_list[index].max = tmp
        if tmp<bucket_list[index].min:
            bucket_list[index].min = tmp
    # 遍历所有桶，比较左桶的最小值与右桶的最大值，得到最大gap
    gap = float('-inf')
    for i in range(n-1):
        if bucket_list[i].min != float('inf'):  # 桶内有元素
            left_max = bucket_list[i].max
        else:   # 遇到空桶，往后继续找非空桶
            continue
        # 左桶找到了，找与之相邻的右桶
        j = i
        while True:
            j +=1
            if bucket_list[j].min != float('inf'):  # 桶内有元素
                right_min = bucket_list[j].min
                break
        if right_min-left_max>gap:
            gap = right_min-left_max
    
    return gap

if __name__ == "__main__":
    input = [20,15,14,10,9,1,0]
    print("无序数组排序后最大相邻差：")
    print(get_maxGap(input))
    