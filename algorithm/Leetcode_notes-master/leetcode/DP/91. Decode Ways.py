'''
dp
初始化 i 的意思是 到第i个 我们有多少种解法
pre是 i-2 个长度的string 有多少种解法
cur 是 i-1个 有多少解法
初始化全为1 因为 pre长度为0 时 解法是1 个 cur表示长度为1 时 解法也是1个
从string的第二个数字开始遍历
每次先检查 目前的数字 是不是0
如果是0 的话 那么我们就可以知道 0 是无效的数字 只能和前一位组合起来形成一个码 并且不会增加新的解法
所以 dp[i] = dp[i-2] 并且还要检查如果之前的数字大于3 或者小于0 都是无效的 因为这样组合起来就变成30 或者 00，可以直接返回0
如果不是0 的话
我们要也要判断之前的数字是不是0 并且 组合起来的数字 是不是在26之内 因为大于26 就无法形成组合
dp[i] = dp[i-1] + dp[i-2] 如果满足以上条件的话 说明 第i个解法 可以把当前的数字单独作为一个解码 加上i-1的 也可以 i-1 和 i组成一个 加上i-2的
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        if int(s[0]) == 0:
            return 0
        length = len(s)
        pre = 1
        cur = 1
        for i in range(1, length):
            temp = cur
            if int(s[i]) == 0:
                cur = pre
                if int(s[i - 1]) >= 3 or int(s[i - 1]) == 0:
                    return 0
            else:
                if int(s[i - 1]) != 0 and int(s[i - 1:i + 1]) <= 26:
                    cur += pre
            pre = temp
        return cur
if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("10"))