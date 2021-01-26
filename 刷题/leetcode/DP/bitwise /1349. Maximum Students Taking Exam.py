class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m = len(seats)
        n = len(seats[0])
        # 总共有这么多状态
        M = 1 << n
        # dp[i][j]表示 前i 行 j 的状态下的 max student,
        dp = [[-1] * M for i in range(m + 1)]
        check = [0]
        # 算出每一行不合法的 状态 将 # 设为 1，当遇到 . 时与运算结果为 0，表示可以坐人
        for i in range(1, m + 1):
            cur = 0
            for j in range(n):
                cur |= (seats[i - 1][j] == "#") << j
            check.append(cur)

        for i in range(1, m + 1):
            for cur_row in range(M):  # 当前row 的当前状态
                # 表示如果当前的状态左右有人，或者当前位置的座位是坏的话, 判断当前row 的当前状态合不合法
                if cur_row & (cur_row >> 1) != 0 or cur_row & check[i] != 0:
                    continue
                # 因为是第一行，所以所有的位置 只要没坏 都能够做
                if i == 1:
                    dp[i][cur_row] = bin(cur_row).count("1")
                    continue

                for last_row in range(M):
                    # 判断上一行的状态 是不是坐了坏的椅子 或者 如果 上一行右上被坐了 或者 上一行左上被坐了的话 跳过
                    # 初始化要设置为-1， 如果设置0的话，前面如果count 计算是0 的话， 会跳过
                    if dp[i - 1][last_row] == -1 or last_row & (cur_row >> 1) != 0 or (last_row >> 1) & cur_row != 0:
                        continue
                    # 当前row 的 当前状态的Maximum Student， 是由前一行的某个状态 加上 当前坐了几个人
                    print(last_row)
                    dp[i][cur_row] = max(dp[i][cur_row], dp[i - 1][last_row] + bin(cur_row).count("1"))
        print(dp)
        return max(dp[m])

