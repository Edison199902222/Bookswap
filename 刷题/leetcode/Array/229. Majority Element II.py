class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2, num1, num2 = 0, 0, 0, 1
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 += 1
            elif count2 == 0:
                num2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return [value for value in (num1, num2) if nums.count(value) > len(nums) // 3]
'''
从题目中我们知道 我们要找到超过数组三分之一的数 那么 这个数 只能最多有两个
所以 我们用 c1，c2，n1，n2 去记录 这两个数 （必须得不一样 初始化的时候， 因为如果两个值初始化一样的话 
比如 [0,0,0] 那么 最后return的结果是[0,0]）
然后 我们遍历数组
如果count 等于 0时， 说明 这个count 没有记录任何数，所以我们把第一个遇到的数字 记录下来 更新num
如果遇到 和 之前相同的数的话， 对应的count 加1
其他情况 就是遇到了其他数 
每遇到一个其他数， 我们就把候选的两个数的 count 进行 - 1 这样操作是因为 每遇到一个其他数 我们可以把之前的数的level下降1 
因为一旦有数字比之前我们的候选者 的数量多的话， 那么之前的数字的数量会下降到0 然后把另一个数组更新成候选数字
'''