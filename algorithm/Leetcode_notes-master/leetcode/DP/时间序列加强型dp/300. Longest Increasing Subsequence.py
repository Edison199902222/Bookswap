
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
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
'''
    二分法思路 
    创建一个都是最大值的array
    遍历我们的数组， 对于数组的每一个元素
    我们在 创建的array中 找到第一个大于等于它的位置
    然后 在 创建的数组中， 检查 非 max 的个数 就是LIS的长度
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return len(nums)
        temp = [float("inf") for i in range(len(nums))]
        for num in nums:
            pos = self.binary_search(temp, num)
            temp[pos] = num
        left = 0
        print(temp)
        while left < len(temp) and temp[left] != float("inf"):
            left += 1
        return left

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS2([10,9,2,5,3,7,101,18]))