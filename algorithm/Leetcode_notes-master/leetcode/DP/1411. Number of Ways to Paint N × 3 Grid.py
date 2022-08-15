class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        two_color = 6
        three_color = 6
        mod = 10**9 + 7
        for i in range(n - 1):
            two_color, three_color = two_color * 3 + three_color *2, two_color * 2 + three_color *2
        return (two_color + three_color) % mod
'''
我们可以算出来
对于第一行row来说
two color 意思是 由两个颜色组成的组合 121 
three color 意思是 三个颜色组成的组合 123 这种
我们可以算出 各有六种
然后对于第二行来说  如果上面一行是 121 之中的某个颜色 下面就有 三种是121 跟两种123 的组合
如果上面一行是 123 中某个颜色 下面就有 两种123 跟两种121 组合 
所以我们不断进行iteration， dp推断 下一层会怎么变化
最后 两种组合加起来就是我们总方法数量了
'''