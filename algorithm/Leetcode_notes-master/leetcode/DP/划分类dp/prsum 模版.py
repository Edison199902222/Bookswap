
# 可以求出当前index为止的subarray中， 最大的subarray值
def get_max(list):
    local_min = 0
    global_max = float("-inf")
    prefix = 0
    left_max = [0 for i in range(len(list))]
    for i in range(len(list)):
        # 先把当前数加上prefix
        prefix += list[i]
        # 然后更新global，用当前总的prefix 减去 前面最小的值
        global_max = max(global_max, prefix - local_min)
        # 更新local min  给下一个更大的subarray
        local_min = min(local_min, prefix)
        # 更新当前为止的global
        left_max[i] = global_max

    return left_max

# 可以求出当前index为止的subarray中， 最小的subarray值
def get_min(list):
    local_max = 0
    global_min = float("inf")
    prefix = 0
    left_max = [0 for i in range(len(list))]
    for i in range(len(list)):
        prefix += list[i]
        global_min = min(global_min, prefix - local_max)
        local_max = max(local_max, prefix)
        left_max[i] = global_min
    return left_max
def main():
    list = [1 ,-1 ,2 ,-4 ,-5 ,6]
    result = get_min(list)
    print(result)

main()

# 找出每个区间的 local_max/ local_min 然后用当前值减去local 就可以去更新global
# 也可以用kadane's algorithm， kadane's algorithm 类似于dp，每次都考虑当前点作为新起点
