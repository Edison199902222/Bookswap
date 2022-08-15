
'''
这道题 dfs 但想法不太一样
意思是 现在围成四条边
每一次递归都看成 把当前火车 尝试去放入四个边里 如果放入的话 就下一根火柴！ 这就是for的作用
'''

class Solution(object):
    def makesquare(self, nums):
        if not nums:
            return False
        sums = sum(nums)
        nums.sort(reverse=True)
        if sums%4 != 0:
            return False
        return self.dfs(nums,0,[0,0,0,0],sums/4)

    def dfs(self,nums,pos,t,target):
        if len(nums) == pos:
            if t[0] == t[1] == t[2]:
                return True
            return False
        for i in range(4):
            if t[i] + nums[pos] > target:
                continue
            t[i] += nums[pos]
            if self.dfs(nums,pos+1,t,target):
                return True
            t[i]-=nums[pos]
        return False


if __name__ == "__main__":
    solution = Solution()
    list1 = [3,3,3,3,4]
    print(solution.makesquare(list1))
