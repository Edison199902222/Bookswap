class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        if nums is None or len(nums) == 0:
            return -1

        n = len(nums)
        minLength = n + 1
        sum = 0
        j = 0
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLength = min(minLength, j - i)

            sum -= nums[i]

        if minLength == n + 1:
            return -1

        return minLength
'''
time O(n)
枚举先
tow point同向双指针
先累加 一旦sums大于等于s了 先把这个length添加进res 并且跟之前的res比较
然后开始缩小范围 用while 在这个区间内不断去缩小length
我们需要不断把 left 往右边移动 因为这样才能使得总体减小
最后检查res是不是跟最大值相等 如果相等说明没有这个值存在
'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSize([2,3,1,2,4,3], 7))