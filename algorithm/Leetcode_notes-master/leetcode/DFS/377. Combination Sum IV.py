class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.dfs(0, target, nums)

    def dfs(self, sums, target, nums):
        if sums > target:
            return 0
        if sums in self.memo:
            return self.memo[sums]
        result = 0
        if sums == target:
            result += 1
        # 完全背包， 所以可以从头到位都遍历！！用sums 作为flag 来memo
        for i in range(len(nums)):
            result += self.dfs(sums + nums[i], target, nums)
        self.memo[sums] = result
        return result


'''
dfs + memo
用memo 因为 【 1，3】 跟【3，1】算不一样的解
如果 不用memo的话 那么会超时
memo中记录的是 每一个target 有多少个解
下次如果遇到同样的数字的话 就可以直接返回了 相当于减枝
'''


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
        # 所谓的bottom up 是对当前target 而言，不是对idnex 而言
        # dp[i] : numbers of ways to get sum
        # target 放在外层循环的话，是一个target的值对应nums所有的值，说的简单点就是这个target的值由nums中的某些组成，所以是有可能重复的
        # 如果target 在内层循环，得到的是去重后的结果。比如target=4，nums[1,2,3]，不去重的话，1,2,1和2,1,1算两种结果，但是去重的话，只能算一种。
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(1, len(nums) + 1):
                if i >= nums[j - 1]:
                    dp[i] += dp[i - nums[j - 1]]

        return dp[target]