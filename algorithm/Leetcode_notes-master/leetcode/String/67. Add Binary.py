'''
使用sums 去检查是不是有进位 检查上一次计算是不是有溢出 每一次 // 2 向下取整
然后从两个字符串 从后往前遍历 每一次把两个字符串 当前数字 还有 上一次溢出来的 进位数字 进行相加
相加过后 取 %2 的 因为要进位
最后检查 sums 是不是等于0 因为 100 100 相加变成 1000
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        sums = 0
        left = len(a) - 1
        right = len(b) - 1
        while left >= 0 or right >= 0:
            sums = sums // 2
            if left >= 0:
                sums += int(a[left])
            if right >= 0:
                sums += int(b[right])
            res += str(sums % 2)
            left -= 1
            right -= 1
        if sums // 2 != 0:
            res += str(sums // 2)
        return res[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11","1"))