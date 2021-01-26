import collections

'''
prefix_sum 代表 一个array 中 其中subarray 的和
sum - prefix_sum = k 说明 这里面有一段连续的subarray 是 = k的
sum - k = prefix_sum 那么问题只要转化成 找到一个prefix_sum的问题了
初始化 我们需要把 prefix_sum = 0 这个状态 放进dic中
因为 如果现在sums = 2 k = 2 的话 这个presum 是0 
所以 每一次 我们找 sum - k 这个 pre sum 有没有在字典中出现过
presum 表示 之前累加的和 

为什么不会重复呢 比如 【1，1，2，2】 k = 3
是因为我们在 每一组subarray 从index 0 到i， 假设 k 是 j 到 i 
我们需要找到存不存在  prefix sum 在这一段array中
所以 对于每一段subarray 我们找 k 一定是由index j ( j < i) 到i 的一段subarray
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = {}
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            if sum not in d:
                d[sum] = 1
            else:
                d[sum] += 1
        return res


if __name__ == "__main__":
    nums = [1, 1, 1]
    solution = Solution()
    print(solution.subarraySum(nums, 2))
