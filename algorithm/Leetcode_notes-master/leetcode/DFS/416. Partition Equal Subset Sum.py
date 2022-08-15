'''
dfs回溯法
一个个去尝试
如果第一个位置不行
那么我们就换一个起始位置去
并且我们需要跳过相同的数字 因为这个位置如果跟前一个位置相同的话 那么没有尝试的必要
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        for i in nums:
            sum+=i
        if sum%2 != 0 :
            return False
        sum /= 2
        return  self.dfs(nums,0,sum)

    def dfs(self,nums,index,target):
        if target == 0:
            return True
        if index >= len(nums) or target < 0:
            return False
        if self.dfs(nums,index+1,target - nums[index]):
            return True
        j = index+1
        while j < len(nums) and nums[j] == nums[index]:
            j+=1
        return self.dfs(nums,j,target)
