'''
关键就是要sort 因为sort数组后
可以check 之前的数字 与目前数字 是不是一样 如果一样 那么我们就跳过
时间复杂度 O(n!)
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.dfs(nums,[])
        return self.res
    def dfs(self,nums,path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]])


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.visited = [False for i in range(len(nums))]
        nums.sort()
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        if len(path) == len(nums):
            self.result.append(path[:])
        for i in range(len(nums)):
            if self.visited[i] == True:
                continue
            if i != 0 and self.visited[i - 1] == False and nums[i] == nums[i - 1]:
                continue
            self.visited[i] = True
            path.append(nums[i])
            self.dfs(nums, path)
            self.visited[i] = False
            path.pop()

