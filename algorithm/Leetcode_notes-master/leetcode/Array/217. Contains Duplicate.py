class Solution:
    def containsDuplicate(self, nums) -> bool:
        if not nums:return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                return True
        return False
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([3,3]))