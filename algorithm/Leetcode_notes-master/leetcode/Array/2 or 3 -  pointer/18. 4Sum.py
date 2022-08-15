'''
也可以使用双之争来解决
需要注意 去掉重复情况！ 用两个loop时 都需要注意去重复
并且 a+b+c+d = target的话
那么第一个for 选取a
第二个for 定住b
然后采用双指针
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sums > target:
                        right -= 1
                    else:
                        left += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    list = [1,0,-1,0,-2,2]
    print(solution.fourSum(list,0))