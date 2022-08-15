class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        prev = [0] * n
        # 记录下，j 的所有前置课程
        for i, j in dependencies:
            prev[j - 1] |= (1 << (i - 1))
        # 记录可以使用的组合 的前置课程
        prev_set = [0] * (1 << n)
        # 表示当前组合是否合法， 0 为合法， 1 为不合法
        check = [0] * (1 << n)

        for mask in range(1 << n):
            # 当前状态可以上的课 在一学期内可以上完
            if bin(mask).count("1") <= k:
                # 拆分当前mask， 把 所有的课的先修课程放进prev中
                for i in range(n):
                    # 看当前的课在不在mask中, 如果在的话，把 第i门的先修课 放进去
                    if mask & (1 << i):
                        prev_set[mask] |= prev[i]
                # 如果一个状态以及包含了部分自己的前导课程，我们就认为是无效的
                check[mask] = ((mask & prev_set[mask]) == 0)

        dp = [n] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            subset = mask
            while subset:
                # 如果是合法的subset 并且子集所需要的先修课，当前状态必须也包含，因为子集如果要转移到mask中，需要先修课满足条件
                if check[subset] and ((mask & prev_set[subset]) == prev_set[subset]):
                    dp[mask] = min(dp[mask], dp[mask ^ subset] + 1)  # 异或是 出去subset 的状态，意思是还没有上subset这几门课的状态
                # 枚举子集， 减1 表示减去最右边一门课， & 保证 不存在mask中的不会选中
                subset = (subset - 1) & mask

        return dp[(1 << n) - 1]
