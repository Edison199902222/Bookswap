class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 代表出现一次的数， 出现两次的数字
        one = two = 0
        for num in nums:
            # x & ~(x) = 0
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one

        return one
'''
举个简单的例子，假设数字5连续出现3次：


第一次、one = 5, two = 0

第二次、one = 0, two = 5

第三次、one = 0, two = 0
'''