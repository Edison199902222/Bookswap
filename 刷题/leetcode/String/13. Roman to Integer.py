'''
从后往前遍历
用max去记录之前的letter 的value 如果遍历到现在的这个字母 比之前的max小
那说明这是一个组合 total就去减去这个字母的数值
'''

class Solution(object):
    def romanToInt(self,s):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        max = 0
        total = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if dic[c] >= max:
                total = total + dic[c]
                max = dic[c]
            else:
                total = total - dic[c]
        return total
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))