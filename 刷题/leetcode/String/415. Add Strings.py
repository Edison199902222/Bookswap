class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ""
        left = len(num1) - 1
        right = len(num2) - 1
        carry = 0
        sums = 0
        while left >= 0 or right >= 0:
            sums = carry
            if left >= 0:
                sums += int(num1[left])
            if right >= 0:
                sums += int(num2[right])
            ans += str(sums % 10)
            carry = sums // 10
            left -= 1
            right -= 1
        if carry != 0:
            ans += str(carry)
        return ans[::-1]
'''
每次使用carry 记录 上一次的 进位情况
然后从后往前加
每次 让sums 等于carry 位 然后再累加
ans 每次 加上 sums % 10 
同时 carry 位要等于 sums // 10 保持进位
最后检查 carry是不是等于0  如果不等于 说明还需要进位 
然后return 反向的 因为我们一直加的时候 是反着的
'''