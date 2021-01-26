class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0 for i in range(length)]
        # 记录每一个index 加value 的情况
        operation = [0 for i in range(length)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            value = updates[i][2]
            # 从start 开始 加value
            operation[start] += value
            # end + 1 开始过期了，不能再加，所以用减
            if end + 1 < length:
                operation[end + 1] -= value
        carry = 0
        # 对每一个index 进行操作
        # 用carry 来记录 加value 的边界
        for i in range(len(result)):
            carry += operation[i]
            result[i] += carry
        return result


'''
做法就是在开头坐标 start 位置加上 inc，而在结束位置 end 加1的地方加上 -inc。
就比如说需要将新区间 [1, 3] 内数字都加2，那么我们在1的位置加2，在4的位置减2，于是数组就变成了 [0, 2, 0, 0, -2]。
经过这个做法 
得到一个累加的数组 
需要注意的是这里 end 可能等于 n-1，则 end+1 可能会越界，所以我们初始化数组的长度为 n+1，就可以避免越界了
累加数组中每个数字代表 当前index 跟 之后的 index 都需要累加上当前数字
然后我们遍历result
result的第一位 初始化因为是0 所以第一位应该是累加数组的第一位相等 因为之前没有累加的数字了
然后后面 每一个数 应该等于前一位的数字加上累加数组中8累加的数字

'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.getModifiedArray(1,[[0,0,-1000]]))