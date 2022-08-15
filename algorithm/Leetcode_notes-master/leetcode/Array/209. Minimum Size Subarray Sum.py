'''
枚举先
tow point同向双指针
先累加 一旦sums大于等于s了 先把这个length添加进res 并且跟之前的res比较
然后开始缩小范围 用while 在这个区间内不断去缩小length
我们需要不断把 left 往右边移动 因为这样才能使得总体减小
最后检查res是不是跟最大值相等 如果相等说明没有这个值存在
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or not s:return 0
        sums = 0
        left = 0
        res = float("inf")
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                res = min(res,i - left +1)
                sums -= nums[left]
                left += 1
        if res == float("inf"):
            return 0
        else:
            return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7,[2,3,1,2,4,3]))