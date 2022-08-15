class Solution:
    def numWays(self, s: str) -> int:
        # 思路： 找到两块板子，插入数组，分成3 组符合题目的数组
        c = collections.Counter(s)
        m = len(s)
        if c["1"] % 3 == 1:
            return 0
        if c["1"] == 0:
            #如果我们把板子选择插在第一个0 后面
            #那么第二个板子 可以插入的option 有n - 2 个
            #where n = s.length(); Similarly, we can choose 2nd 0, we have n - 3 options, ...,
            # 所以 每次 (n-2) + (n - 3) + (n - 4) + ... 1 等差数列求和
            # etc, totally, the result is (n - 2) * (n - 1) / 2
            return (m - 2) * (m - 1) // 2 % (10 ** 9 + 7)
        # 如果不是全0的情况
        first = 0
        second = 0
        # 先求出每个数组需要几个1
        n = c["1"] // 3
        # 第一块板子可以插的范围是在 满足第一个数组的1 跟 第二个数组开始位置 中间的间隔
        # 第二块板子可以插的范围是 满足第二个数组的1 出现的次数 跟第三个数组开始的位置 中间的间隔
        # 两个相乘就是总共的组合， 跟全是0情况不一样的是 100， 可以插3 次，因为板子也可以插在最后一个0 的后面
        sums = 0
        for i in range(len(s)):
            sums += int(s[i])
            if sums == n:
                first += 1
            if sums == n * 2:
                second += 1
        return first * second