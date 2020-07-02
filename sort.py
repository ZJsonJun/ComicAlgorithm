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
    for _ in range(len(data)-1):
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

def quick_sort_stack(start_index: int,end_index: int,array: []):
    """
    快速排序（栈实现）
    """
    # 创建一个栈，保存递归调用函数的参数
    stack = []
    # 整个数组的起始和终止下标，以key-value形式入栈
    root_param = {"start_index":start_index, "end_index":end_index}
    stack.append(root_param)
    # 循环结束条件： 栈为空时结束
    while len(stack)>0:
        # 栈顶元素出栈，得到起始和终止下标
        param = stack.pop()
        pivot_index = partition_v2(param.get("start_index"),param.get("end_index"),array)
        # 根据基准元素位置，把剩下数组划分为两部分，并将每部分的起止下标入栈
        if param.get("start_index")<pivot_index-1:
            left_param = {"start_index":param.get("start_index"), "end_index":pivot_index-1}
            stack.append(left_param)
        if param.get("end_index")>pivot_index+1:
            right_param = {"start_index":pivot_index+1, "end_index":param.get("end_index")}
            stack.append(right_param)

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

def heap_sort(array: []):
    """
    堆排序（从小到大排序，需要构建最大堆）
    """
    build_heap(array,len(array))
    # 交换堆顶元素与堆尾元素(将大节点集中在堆尾)
    for tail in range(len(array)-1,0,-1):
        tmp = array[0]
        array[0] = array[tail]
        array[tail] = tmp
        # 重新构建堆(下沉根节点)
        down_adjust(array,0,tail)

def build_heap(array: [], spec_len: int):
    """
    构建最大堆，可以指定构建区域
    """
    # 依次对每个非叶子节点进行下沉操作
    for i in range((len(array)-2)//2,-1,-1):
        down_adjust(array,i,spec_len)

def down_adjust(array: [],index: int, spec_len: int):
    """
    下沉操作(小节点下沉),改造了下，可以指定待调整数组长度（区域）
    """
    while index*2+1<spec_len or index*2+2<spec_len:
        # 存在左右子节点
        if index*2+2<spec_len:
            swap_index = index*2+1 if array[index*2+1]>array[index*2+2] else index*2+2
            if array[index]<array[swap_index]:
                tmp = array[index]
                array[index] = array[swap_index]
                array[swap_index] = tmp
                index = swap_index
            else:
                break
        # 只存在左子节点
        else:
            if array[index]<array[index*2+1]:
                tmp = array[index]
                array[index] = array[index*2+1]
                array[index*2+1] = tmp
                index = index*2+1
            else:
                break
        


if __name__ == "__main__":
    input = [12,1,11,9,1,2,4,8,9,3,6,7,20,100,10,201,45,2,3,47,99,88,77,12,89]
    print("排序前数组：")
    print(input)
    # quick_sort_stack(0,len(input)-1,input)
    heap_sort(input)
    print("排序后数组：")
    print(input)