
'''
每次往深里搜索
需要一个index变量为了防止重复添加 每次需要把当前的i 去加1 是因为 防止重复进行添加
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, result, [], 0)
        return result

    def dfs(self, nums, result, path, index):
        result.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, result, path + [nums[i]], i + 1)

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        if not nums:
            return []
        self.dfs(nums, 0, [])
        return self.result
    def dfs(self, nums, index, path):
        self.result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+1, path)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))