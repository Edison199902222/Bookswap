class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 需要逆着看
        # 既然每次移动都是让剩余n - 1个数增加1，那么实际就是让选定的那一个数减少1了，
        # 比如上例中的[1, 2, 3] => [1, 1, 3] => [1, 1, 2] => [1, 1, 1]。既然想要知道让数组元素全部相等的最小移动次数，
        # 那么就是所有元素与最小元素的差的和了。
        min_number = min(nums)
        result = 0
        for i in range(len(nums)):
            result += (nums[i] - min_number)
        return result
