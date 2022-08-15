
'''
每次从第i个开始 因为没有重复 并且 我们可以重复利用这些数字重的数字
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates,0,target,[],res)
        return res

    def dfs(self,candidates,index,target,path,res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index,len(candidates)):
            self.dfs(candidates,i,target - candidates[i], path + [candidates[i]], res)


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(candidates, target, 0, [])
        return self.result
    def dfs(self, nums, target, index, path):
        if sum(path) > target:
            return
        if sum(path) == target:
            self.result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, target, i, path)
            path.pop()
if __name__ == '__main__':
    solution = Solution2()
    print(solution.combinationSum([2,3,6,7],7))