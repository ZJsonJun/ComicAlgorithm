"""
最大公约数问题
"""

def get_greatest_common_divisor_v1(a: int, b:int):
    """
    辗转相除法求最大公约数（递归实现）
    """
    # 特殊情况
    if a==0:
        return b
    if b==0:
        return a
    # 一般情况
    if a%b == 0:
        return b
    else:
        return get_greatest_common_divisor_v1(b, a%b)

def get_greatest_common_divisor_v2(a: int, b:int):
    """
    辗转相除法球最大公约数（循环实现）
    时间复杂度：O(log(max(a,b)))
    """
    # 特殊情况
    if a == 0:
        return b
    if b == 0:
        return a
    # 一般情况
    if a%b == 0:
        return b
    else:
        while True:
            tmp = a%b
            if tmp == 0:
                return b
            a = b
            b = tmp
            
def get_greatest_common_divisor_v3(a: int, b:int):
    """
    更相减损术（循环实现）
    时间复杂度：O(max(a,b))
    """
    # 特殊情况
    if a == 0:
        return b
    if b == 0:
        return a
    # 一般情况
    if a == b:
        return a
    big = max(a,b)
    small = min(a,b)
    while True:
        c = big-small
        big = max(c,small)
        small = min(c,small)
        if big == small:
            return big

def get_greatest_common_divisor_v4(a: int, b:int):
    """
    更相减损术（递归实现）
    时间复杂度：O(max(a,b))
    """
    # 特殊情况
    if a == 0:
        return b
    if b == 0:
        return a
    # 一般情况
    if a==b:
        return a
    else:
        big = max(a,b)
        small = min(a,b)
        c = big-small
        return get_greatest_common_divisor_v4(c,small)

def gcd(a: int, b:int):
    """
    最终版求两数最大公约数算法，在更相减损术基础上采用了位运算进行优化`
    """
    # 特殊情况
    if a == 0:
        return b
    if b == 0:
        return a
    # 一般情况
    if a == b:
        return a
    elif (a&1)==0 and (b&1)==0:
        return 2*gcd(a>>1,b>>1)
    elif (a&1)==0 and (b&1)!=0:
        return gcd(a>>1,b)
    elif (a&1)!=0 and (b&1)==0:
        return gcd(a,b>>1)
    else:
        big = max(a,b)
        small = min(a,b)
        c = big-small
        return gcd(small,c)

def gcd_v1(a: int, b:int):
    """
    循环实现
    """
    # 特殊情况
    if a == 0:
        return b
    if b == 0:
        return a
    # 一般情况
    count = 0
    if a == b:
        return a
    while True:
        if (a&1)==0 and (b&1)==0:
            count += 1  # 计数进入此分支多少次
            a = a>>1
            b = b>>1
        elif (a&1)==0 and (b&1)!=0:
            a = a>>1
        elif (a&1)!=0 and (b&1)==0:
            b = b>>1
        else:
            big = max(a,b)
            small = min(a,b)
            c = big-small
            a = small
            b = c
        if a == b:
            return a*2**count
    
if __name__ == "__main__":
    # print(get_greatest_common_divisor_v4(41,11123))
    # print(get_greatest_common_divisor_v1(1211313133133,2**10000))
    print(gcd_v1(12,20))