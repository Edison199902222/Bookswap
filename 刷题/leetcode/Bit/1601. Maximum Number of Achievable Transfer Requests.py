class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        length = len(requests)
        result = 0
        # 每个rqeuest 都可以选/不选
        # 所以用暴力枚举，枚举每一种组合，所以有2 ** length 种组合
        # 用二进制代表 每种组合选取的情况，1 代表选
        for i in range(1 << length):
            # 宿舍进出情况
            count = [0 for i in range(n)]
            for j in range(length):
                # 遍历request，看当前的request 是否被选，选了的话，那么对应的 宿舍的情况要进行改变
                if i & (1 << j):
                    count[requests[j][0]] -= 1
                    count[requests[j][1]] += 1
            # 如果宿舍进出情况还是0，说明这种组合是满足题目条件的
            if max(count) == 0:
                # 更新最大值，数有几个1
                result = max(result, bin(i).count("1"))
        return result
