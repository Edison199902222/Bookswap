class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 本题不同的顺序的组合会看成不同的组合
        # 而普通的完全背包，不同顺序的组合 看作成同一种组合
        # 所以，完全背包内外顺序调换
        dp = [0]* (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(1, len(nums) + 1):
                if i >= nums[j - 1]:
                    dp[i] += dp[i - nums[j - 1]]
        return dp[target]