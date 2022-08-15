'''
首先我们设置一个结果的长度
两个数相乘的结果的长度 不会超过两个数的长度相加
所以我们先设置一个 由0 组成 的list 作为我们的结果
然后 我们进行模拟计算
每次两个数字相乘 我们就有 low 跟 high 位
low 表示的 低位
high 表示高位
每一次进行计算时 我们都需要把当前的位数的low位加起来 因为 现在的low位 就是前一步计算的high 位
然后 低位数要 %10 高位数直接进行//10
最后 因为有可能 有0005的情况
所以我们要把0 给处理掉 
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        l3 = l1 + l2
        ans = [0] * l3
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                temp_result = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                low = i + j + 1
                high = i + j
                temp_result += ans[low]
                ans[low] = temp_result % 10
                ans[high] += temp_result // 10
        result = ""
        lead_zero = 0
        while lead_zero < len(ans) and ans[lead_zero] == 0:
            lead_zero += 1
        ans = ans[lead_zero:]
        for i in range(len(ans)):
            result += str(ans[i])
        if not result:
            return "0"
        else:
            return result


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        l3 = l1 + l2
        res = [0 for i in range(l3)]

        for i in range(l1 - 1, -1, -1):
            carry = 0
            for j in range(l2 - 1, -1, - 1):
                # 算出低位
                res[i + j + 1] += carry + (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                carry = res[i + j + 1] // 10
                res[i + j + 1] %= 10
            res[i] = carry
        i = 0
        while i < l3 and res[i] == 0:
            i += 1
        res = res[i:]
        return '0' if not res else ''.join(str(i) for i in res)