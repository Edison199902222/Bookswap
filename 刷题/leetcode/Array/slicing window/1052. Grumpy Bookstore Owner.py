class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        left = 0
        angry = 0
        result = 0
        for right in range(len(customers)):
            if grumpy[right] == 1:
                angry += customers[right]
            result = max(result, angry)
            if right >= X - 1:
                if grumpy[right - X + 1] == 1:
                    angry -= customers[left]
                left += 1
        for i in range(len(customers)):
            if grumpy[i] == 0:
                result += customers[i]
        return result


'''
窗口题
思路： 我们在 窗口长度为X 的范围内， 找出在窗口内 最大可以把多少个angry 的变成 满意
然后 我们在 遍历一遍，本来满意的顾客有多少个
相加就行了
'''