class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        n = len(nums)
        # 通过交换数字，把index 上的每个数 都填上对应的数字
        # index 0，1，2 对应数字 1，2，3
        # 遍历元素，遍历到的每一个位置上的元素 都让它去对应的地方，只管正数
        # 第二遍遍历，就可以找到缺失的元素， 对应元素范围是[1, n]
        while index < n:
            # 如果发现index 当前位是正数，and index 对应的数字不是对应的数字， and index 的元素 -1 对应的index 不等于 index 的元素
            # 交换两者，让index 位置上的元素 去对应的地方
            while 0 < nums[index] <= n and nums[index] != index + 1 and nums[nums[index] - 1] != nums[index]:
                j = nums[index] - 1
                nums[index], nums[j] = nums[j], nums[index]
            index += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        result = [None for i in range(len(nums))]
        for i in range(len(nums)):
            if len(result) >= nums[i] > 0:
                result[nums[i] - 1] = nums[i]

        for i in range(len(result)):
            if result[i] == None:
                return i + 1
        return len(result) + 1

