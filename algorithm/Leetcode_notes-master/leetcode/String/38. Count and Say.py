'''
两个指针
指针pre 记录之前的 数字 并且检查与下一个指针的元素是不是一样的
然后count 记录的是pre 出现了几次 如果发现之前的元素跟下一个元素是相同的 那就+1
发现pre跟现在元素不同时 说明之前元素统计已经结束 可以添加进新的字符串之中了
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 这题目描述非常不清晰，举个例子， 21 变成 1211，是 由 一个二，一个一，所以是 1211
        # 就是 count（这个数字有几个） + 数字， 下一层 是由当前这一层的数字 推出来的
        if not n:
            return ""
        string = "1"
        for i in range(n - 1):
            count = 1
            prev = string[0]
            cur = ""
            # 数prev 这个数字有几个，如果prev 跟当前数字不一样，证明prev 数字结束了，把答案放进cur 中
            # 循环结束后，因为最后一个数字还没有放，所以再放一次
            for i in range(1, len(string)):
                if prev != string[i]:
                    cur = cur + str(count) + prev
                    count = 1
                    prev = string[i]
                else:
                    count += 1
            cur = cur + str(count) + prev
            string = cur
        return string
