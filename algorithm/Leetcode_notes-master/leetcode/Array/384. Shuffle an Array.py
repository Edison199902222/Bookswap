import random
'''
洗牌的意思是 重新调整顺序 并且每次不能重复
洗牌时 我们只需要每次选取0 ～ index 长度的随机数字 然后交换最后一位 跟 随机数字 两个的位置
每次 随机数字-1 这样就避免了重复
'''
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.length = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.original.copy()
        idx = self.length - 1
        for i in range(self.length):
            random_num = random.randint(0,idx)
            res[random_num],res[idx] = res[idx],res[random_num]
            idx -= 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()