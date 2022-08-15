'''
跟上一道题 差不多
但是要多加一个情况
因为这道题有重复的数字
如果出现重复的数字的时候 也就是mid 跟 low相等时 我们把start+1就行 这样可以重置start跟mid
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[low]:
                if nums[mid] >= target and target >= nums[low]:
                    high = mid -1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid - 1
            else:
                low +=1
        return False
if __name__ =="__main__":
    solution = Solution()
    print(solution.search([1,3,1,1,1],3))