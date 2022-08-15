
'''
这道题 需要output 里面的数字 都是独一无二的 unique的
所以 在进行递归的时候 我们的index 需要i+1 而不是index+1 i+1 意思是 除去当前的数字

'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1,10),k,n,0,[],res)
        return res

    def dfs(self,nums,k,n,index,path,res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums, k-1, n - nums[i], i+1, path + [nums[i]],res)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(k,n,[],1)
        return self.result
    def dfs(self,k, n, path, index):
        if sum(path) > n or len(path) > k:
            return
        if sum(path) == n and len(path) == k:
            self.result.append(path[:])
            return
        for i in range(index, 10):
            path.append(i)
            self.dfs(k, n, path, i + 1)
            path.pop()
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum3(3,7))


