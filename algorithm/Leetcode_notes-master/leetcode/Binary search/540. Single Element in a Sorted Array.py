class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mid % 2 == 0:
                if mid + 1 <= n - 1 and nums[mid] != nums[mid + 1]:
                    end = mid
                else:
                    start = mid
            else:
                if mid - 1 >= 0 and nums[mid] != nums[mid - 1]:
                    end = mid
                else:
                    start = mid
        if start % 2 == 0:
            if start + 1 <= n - 1 and nums[start] != nums[start + 1]:
                return nums[start]
            else:
                return nums[end]
        else:
            if start - 1 >= 0 and nums[start] != nums[start - 1]:
                return nums[start]
            else:
                return nums[end]

'''
当mid 的index 是even的时候， 理论上 mid 应该跟 mid+1 数值相同
如果 不相同 或者 mid已经是数组中可以遍历的最后一个数字了 那说明 答案在左边
相同的话 说明在右边
当mid 的index 是odd的时候， 理论上 mid 应该跟 mid-1 数值相同
如果 不相同 或者 mid已经是数组中最左边能到的数字了 那说明 答案在左边
相同的话 说明在右边
然後當start是even, 就跟後一個nums[start+1]比看是否相同
->是, 回傳nums[end]
->不是, 回傳nums[start]
同理, 當start是odd, 跟前一個nums[start-1]比看是否相同
->是, 回傳nums[end]
->不是, 回傳nums[start]
'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))