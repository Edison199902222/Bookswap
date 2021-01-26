class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        zero_list = [0 for i in range(m)]
        # 统计这每一行，后缀为0的个数
        for i in range(m):
            j = n - 1
            count = 0
            while j >= 0 and grid[i][j] == 0:
                count += 1
                j -= 1
            zero_list[i] = count
        result = 0
        for i in range(m):
            # 当前行需要几个后缀0
            need_zero = n - i - 1
            j = i
            while j < len(zero_list) and need_zero > zero_list[j]:
                j += 1
            # 说明没有满足条件的
            if j == len(grid):
                return - 1
            # 操作次数增加
            result += j - i
            while j > i:
                zero_list[j], zero_list[j - 1] = zero_list[j - 1], zero_list[j]
                j -= 1
        return result

