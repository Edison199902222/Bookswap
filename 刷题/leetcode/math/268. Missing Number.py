class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)+1
        sums = 0
        for i in range(1,length):
            sums+=i
        for j in nums:
            sums-=j
        return sums

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([1,2,3,0]))