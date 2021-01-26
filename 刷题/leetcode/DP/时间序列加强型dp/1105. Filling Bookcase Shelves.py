class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        # dp[i] 表示 第i 本书是本层最后一本书 能组成的最低高度
        # 加一个是为了好算dp
        books.insert(0, [0, 0])
        dp = [float("inf")] * (n + 1)

        dp[0] = 0
        # i 是本层最后一本书
        for i in range(1, n + 1):
            # 找上一层最后一本书
            # 把第i 本书 设置成当前层最后一本书
            cur_width = books[i][0]
            max_height = books[i][1]
            # 先更新这一层只有 i 这一本书的情况
            dp[i] = dp[i - 1] + max_height
            # 把j 加入本层，那么j - 1就是上一层最后一本书
            for j in range(i - 1, 0, -1):
                cur_width += books[j][0]
                max_height = max(max_height, books[j][1])
                if cur_width <= shelf_width:
                    dp[i] = min(dp[i], dp[j - 1] + max_height)
                else:
                    break
        return dp[n]


class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        # dp[i] 表示 第i 本书是本层最后一本书 能组成的最低高度
        # 加一个是为了好算dp
        dp = [float("inf")] * (n + 1)

        dp[0] = 0
        # i 是本层最后一本书
        for i in range(1, n + 1):
            # 找上一层最后一本书
            # 把第i 本书 设置成当前层最后一本书
            cur_width = books[i - 1][0]
            max_height = books[i - 1][1]
            # 先更新这一层只有 i 这一本书的情况
            dp[i] = dp[i - 1] + max_height
            # 把j 加入本层，那么j - 1就是上一层最后一本书
            for j in range(i - 1, 0, -1):
                cur_width += books[j - 1][0]
                max_height = max(max_height, books[j - 1][1])
                if cur_width <= shelf_width:
                    dp[i] = min(dp[i], dp[j - 1] + max_height)
                else:
                    break
        return dp[n]


