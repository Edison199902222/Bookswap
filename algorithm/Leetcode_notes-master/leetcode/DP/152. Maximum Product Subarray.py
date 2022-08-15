class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: return 0
        dp = [[0 for i in range(2)]for i in range(2)]
        dp[0][0],dp[0][1],res = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            x,y= i%2,(i-1)%2 #表示要么是0，要么是1 x表示的是现在的 y表示之前的
            dp[x][0] = max(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
            dp[x][1] = min(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
            res = max(dp[x][0],res)
        return res