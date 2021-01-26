'''
For the complexity, I think you can explain in this way: in the first level of the tree,
you have N options and for each of the option, you have N-1 option, and for each of these N-1 options,
 you have another N-2 options, so putting them together you would end up N*(N-1)*(N-2).... = N!
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        path = []
        self.dfs(nums, path)
        return self.result

    def dfs(self, nums, path):
        if not nums:
            self.result.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]])


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        if len(path) == len(nums):
            self.result.append(path[:])

        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.dfs(nums, path)
            path.pop()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.visited = [False for i in range(len(nums))]
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        if len(path) == len(nums):
            self.result.append(path[:])

        for i in range(len(nums)):
            if self.visited[i]:
                continue
            self.visited[i] = True
            path.append(nums[i])
            self.dfs(nums, path)
            self.visited[i] = False
            path.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
