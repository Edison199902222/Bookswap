'''
我们需要要得到char 首先要用chr
要用n-1 %26 这样才能得到正确的值
其次为什么最后要reverse 因为这样是从后往前取的
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            res.append(chr((n-1)%26 + ord("A")))
            n = (n-1) // 26
        res.reverse()
        return "".join(res)


class Solution:
    def convertToTitle(self, n: int) -> str:
        string = []
        while n:
            digit = n % 26
            if digit == 0:
                # 当 n是26 的倍数的时候，需要z
                # 为什么要减26， 因为n = 26 的时候，n如果只//26 会等于1， 会多加一个
                string.append("Z")
                n -= 26
            else:
                string += (chr(ord("A") + digit - 1))
            n //= 26
        return "".join(reversed(string))


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(28))
