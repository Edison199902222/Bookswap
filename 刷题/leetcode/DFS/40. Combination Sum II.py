'''
每次 需要检查 如果大于起点 为什么需要大于起点 因为如果 当前的i 跟 i-1 指向数字是一样的 但是不在我们的区间范围之内 i是不需要跳过的
 并且 这个的数字 与之前的数字相等 那么我们就需要跳过 因为不能有重复的
并且index + 1
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates, index, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, i + 1, target - candidates[i], path + [candidates[i]], res)


class Solution2:
    def combinationSum2(self, candidates, target):
        self.result = []
        candidates.sort()
        self.dfs(candidates, [], 0, target)
        return self.result
    def dfs(self, nums, path, index, target):
        if sum(path) > target:
            return
        if sum(path) == target:
            self.result.append(path[:])
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, path, i+1, target)
            path.pop()
'''
没重复的元素 想要不重复的解 index单调向前
有重复的元素 想要不重复的解 一个for之中 一个元素 只添加一次 所以要检查是不是跟之前的元素相同
'''