class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.dfs(nums, 0, [])
        return self.result

    def dfs(self, nums, index, path):
        self.result.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path)
            path.pop()
'''
有重复元素 避免重复的解
那就先sort之后 
每次注意 避免上一步相同的元素就行
'''