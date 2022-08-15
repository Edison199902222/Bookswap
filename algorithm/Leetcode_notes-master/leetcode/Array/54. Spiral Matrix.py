class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        row_begin = 0
        row_end = len(matrix) - 1
        col_begin = 0
        col_end = len(matrix[0]) - 1
        result = []
        while row_begin <= row_end and col_begin <= col_end:
            for i in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            # 根据观察，如果row end 大于等于 begin 的时候，才说明有一行可以从后往前 输出
            # 因为想象一下，只有把row start 跟row end 想象成两根线
            # 现在要从 end 这跟线 往左移动到 start， 那么只有start < end 的时候 才会继续输出
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, - 1):
                    result.append(matrix[row_end][i])
            # 想象col begin 根 col end 想象乘两个横线
            # 现在要从 end 到begin， 往上移动， 那么只有 start < end 的时候，才会继续输出
            row_end -= 1
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][col_begin])
            col_begin += 1
        return result


'''
维护四个边界和运动方向
四个边界分别是 row 的起始 跟 结束  col的起始 跟结束
从左向右边打印 然后第一行打印完 我们的row起始需要加1 因为下次打印最右边时 我们需要从row的起始 +1的地方开始打印
然后从上到下 把最右边打印完 我们的col 结束 需要减去1 因为下次打印从最下面 右边往左边时 我们需要从col 的结束 - 1的地方开始打印
我们还需要 检查 此时如果想从右到左打印 是不是还有row 给我们打印
    然后从右到左 把最下面打印完 我们的row 结束 需要-1 
检查是不是又col 给我们打印
然后从下岛上 把最左边打印完 我们的col 起始需要 +1 

'''