'''
用一个字典
储存目前第i个数字 所需要凑成taget的数字 并且把index对应
然后如果在遍历这个数组的时候 出现了字典里需要的数字 直接return
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11],9))