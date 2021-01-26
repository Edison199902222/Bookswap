'''
首先 是必定存在一个峰值
　根据对半分的思路继续想，不难发现只要确定了中间位置的数是处在上升阶段还是下降阶段，就可以确定在某一侧必有一个峰值
我们从中得到mid
mid 如果 大于mid-1 说明这个峰值在右边
mid 如果小于mid-1 峰值肯定在左边

最后的情况是用来检查，如果当前的数组情况 小于3 的时候 比如[1,2]的时候 怎么办
还有比如 [1,2,3]没有所谓的峰值的时候，我们的return 最后一个
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return - 1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # 处于上升阶段，右边有peak
            elif nums[mid] > nums[mid - 1]:
                left = mid
            # 处于下降阶段，左边有peak
            else:
                right = mid
        if nums[left] >= nums[right]:
            return left
        else:
            return right


if __name__ == "__main__":
    soluiton = Solution()
    print(soluiton.findPeakElement([1,2,1]))
