
'''
dp
其实就是dp加双指针
题目要求的意思是， 以i 为结尾 的最大子序列， i 的index 是子序列中最大的 index
初始化dp， 对于每个位置来说， 自身就是一个上升的子序列 所以 初始化为1
dp[i] 表示 以index i 的值作为结尾 的最长上升子序列
那么遍历 数组 把每一个元素 i 当成子序列中的最后一个元素
然后再遍历 i 前面 的元素
如果我们发现 i 前面的元素j是小于 i的话， 就说明我们可以把i 放进dp[j]中， 也就是以j 为结尾的最大子序列
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if  nums is None or not nums: return 0
        n = len(nums)
        dp = [1 for _ in xrange(n)]
        res = 1
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res

    def lengthOfLIS2(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size # 一开始tail数组只有一个数字
            while i < j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size) # 只有i移动到数组末尾 才说明size+1了 不然会维护之前的size不变
        return size
if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS2([10,9,2,5,3,7,101,18]))