class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        if max(nums) < 0:
            return max(nums)
        local_max,global_max = 0,0
        for i in range(len(nums)):
            local_max = max(0,nums[i]+local_max)
            global_max = max(local_max,global_max)
        return global_max
'''
local记录 只要当前加起来的数字大于0 我们就记录
每次local 更新后 就说明有新的sum 出现了 那么我们就用global 来判断
global 记录之前local 最大值 与现在local的值 进行比较

'''