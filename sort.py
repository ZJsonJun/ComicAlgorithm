"""
一些排序算法
"""

def bubble_sort_v1(data: []):
    """
    原始的冒泡排序算法
    """
    if len(data)==0:
        print("空数组！！!")
        return
    # 总共需要排序轮次
    for i in range(len(data)-1):
        # 每轮次需要比较的次数
        for j in range(len(data)-1-i):
            if data[j]>data[j+1] :
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp

def bubble_sort_v2(data : []):
    """
    改进的冒泡排序算法
    改进点：若已经有序，则提前终止，减少无用的循环次数
    """
    if len(data)==0:
        print("空数组！！!")
        return
    for i in range(len(data)-1):
        # 先将flag置位
        is_sorted = True
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
                # 发生了交换，说明还不能肯定完全有序
                is_sorted = False
        # 如上一轮次没有发生交换，则说明数组已经有序
        if is_sorted:
            break

def bubble_sort_v3(data : []):
    """
    改进的冒泡排序算法
    改进点1：若数组已经有序，则提前终止
    改进点2：记录最后一次元素交换的位置，作为无序区边界
    """
    if len(data)==0:
        print("空数组！！!")
        return
    # 无序区边界
    set_border = len(data)-1
    # 记录最后一次交换位置
    last_swap_index = 0
    for i in range(len(data)-1):
        # 先将flag置位
        is_sorted = True
        for j in range(set_border):
            if data[j]>data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
                # 发生了交换，说明还不能肯定完全有序
                is_sorted = False
                last_swap_index = j
        # 设置无序区边界
        set_border = last_swap_index
        if is_sorted:
            break

def cock_tail_sort(data : []):
    """
    鸡尾酒排序（秘诀就是摇晃）
    """
    if len(data)==0:
        print("空数组！！!")
        return
    for i in range(len(data)//2):
        # 有序标记 初始为True
        # 偶数轮次(0 开始)
        is_sorted = True
        for j in range(i,len(data)-1-i):
            if data[j]>data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
                is_sorted = False
        if is_sorted:
            break
        # 奇数轮次（1 开始）
        is_sorted = True
        # 这边较原始代码改进了一点，就是在偶数轮次结束后，无序区长度应该减少了1，所以这里减2
        for j in range(len(data)-2-i,i,-1):
            if data[j]<data[j-1]:
                tmp = data[j]
                data[j] = data[j-1]
                data[j-1] = tmp
                is_sorted = False
        if is_sorted:
            break

def quick_sort(start_index: int,end_index: int,array: []):
    """
    快速排序（递归实现）
    """
    # 出口条件
    if start_index>=end_index:
        return
    # 定位基准元素放置位置
    pivot_index = partition_v2(start_index,end_index,array)
    # 分治
    quick_sort(start_index,pivot_index-1,array)
    quick_sort(pivot_index+1,end_index,array)

def partition_v1(start_index: int,end_index: int,array: []):
    """
    双边循环法，定位基准元素放置位置（快排）
    """
    # 选择数组首元素作为基准元素
    pivot = array[start_index]
    left = start_index  # 左指针
    right = end_index   # 右指针
    while(left != right):
        # 先尝试移动右指针
        while left<right and array[right]>pivot:
            right-=1
        # 尝试移动左指针
        while left<right and array[left]<=pivot:
            left+=1
        # 交换左右指针所指向元素
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp
    # 交换pivot 到左右指针重合的位置（其在有序数组中的位置）
    array[start_index] = array[left]
    array[left] = pivot
    return left

def partition_v2(start_index: int,end_index: int,array: []):
    """
    单边循环法，定位基准元素放置位置（快排）
    """
    # 选择数组首元素作为基准元素
    pivot = array[start_index]
    # 标记小于基准元素区域边界
    mark = start_index
    for i in range(start_index+1,end_index+1):
        if array[i]<pivot:
            mark+=1
            tmp = array[i]
            array[i] = array[mark]
            array[mark] = tmp
    # 最后将pivot 交换到基准位置
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark


if __name__ == "__main__":
    input = [12,1,11,9,1,2,4,8,9,3,6,7,20,100,10,201,45,2,3,47,99,88,77,12,89]
    print("排序前数组：")
    print(input)
    quick_sort(0,len(input)-1,input)
    print("排序后数组：")
    print(input)