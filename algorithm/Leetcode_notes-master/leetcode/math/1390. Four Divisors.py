import math

'''
不能暴力解
我们可以从数学推断出
一个数字 x = a * b
假设 a <= b  那么 a最大的情况是 a = b 
也就是 最大的情况下 a = x^0.5
那么我们找到了a的范围， 然后只要找到了a 我们就能找到b
b = x // a
这样我们就缩小了范围 找到了a 就找到了b
'''
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        for i in range(len(nums)):
            temp = set()
            temp.add(1)
            temp.add(nums[i])
            number_divide = 2
            for j in range(2, int(math.sqrt(nums[i])) + 1):
                if nums[i] % j == 0:
                    if j * j == nums[i]:
                        number_divide += 1
                        temp.add(j)
                    else:
                        number_divide += 2
                        temp.add(j)
                        temp.add(nums[i] // j)
                if number_divide > 4:
                    break
            if number_divide == 4:
                sums += sum(temp)
        return sums




