'''
用的是greedy的方法
用两个变量 来记录 之前最小 跟第二小的 如果再出现一个比他们两个都大 说明这个是increasing的
每次 如果数字比最小的还要小 就更新最小的
记得一开始初始值一定要设置为最大值
'''


class Solution:
    def increasingTriplet(self, nums) -> bool:
        if not nums:return False
        first = second = float('inf')
        for i in range(len(nums)):
            if nums[i] < first:
                first = nums[i]
            elif first < nums[i] < second:
                second = nums[i]
            elif nums[i] > second:
                return True
        return False
if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet([1,2,3,4,5]))