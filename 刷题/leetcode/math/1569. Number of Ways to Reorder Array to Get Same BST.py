class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        return self.helper(nums) - 1

    def helper(self, nums):
        if not nums:
            return 1
        # 首元素
        pivot = nums[0]
        # 小于 root的
        nums_left = [num for num in nums if num < pivot]
        # 大于root 的
        nums_right = [num for num in nums if num > pivot]
        # 最后算 从 除去root 的数量中取 nums left 数量个 作为左边，有几种排列方式 因为是排列组合，算左边还是右边一样的
        return (self.combination(len(nums) - 1, len(nums_left)) * self.helper(nums_left) * self.helper(nums_right)) % (
                    10 ** 9 + 7)

    # 从m 中物品 选n个 公式
    def combination(self, m, n):
        return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))