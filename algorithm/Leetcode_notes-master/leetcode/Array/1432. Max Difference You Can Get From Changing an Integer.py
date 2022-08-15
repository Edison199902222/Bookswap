class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = b = str(num)
        for i in a:
            if i != "9":
                a = a.replace(i, "9")
                break
        if b[0] != "1":
            b = b.replace(b[0],"1")
        else:
            for i in b[1:]:
                if i not in "01":
                    b = b.replace(i,"0")
                    break
        return int(a) - int(b)
'''
为了最大化 a 最小化b
最大化a的方法是 从左到右找到第一个不为9的数字 替换成 9
最小化b 的方法是 如果第一位数不是1 那么把这个数字替换成1
如果第一位数是1 的话 那么从第二位数开始找 第一个不为0 或者1的数字替换成 0
为什么要不为1 呢 因为一旦替换了1 那么所有的1 都会被替换 也就是 第一位数也会被替换成0 这是不合法的, 因为有效操作是把num中 所有i 替换成 x
'''