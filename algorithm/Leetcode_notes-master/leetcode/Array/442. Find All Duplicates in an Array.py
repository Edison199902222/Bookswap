class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        result = []
        for num in nums:
            num = abs(num)
            # 把num - 1 作为坐标，来判断当前num是不是出现了一次
            if nums[num - 1] < 0:
                result.append(num)
            else:
                nums[num - 1] = - nums[num - 1]
        return result


'''
因为 数字的值是从1 到 n
所以 我们 每一次遇到数字
把数字的值 - 1 作为index， 然后把这个index上的值取反
如果下一次 我们遇到同样的数字的话， 会先检查index上的值 是不是负数 如果是负数
说明当前数组遇到第二次了
'''