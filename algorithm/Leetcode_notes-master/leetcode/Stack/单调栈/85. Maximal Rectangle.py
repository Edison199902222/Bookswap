class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        max_rectangle = 0
        height = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                if num == "0":
                    height[index] = 0
                else:
                    height[index] += 1
            max_rectangle = max(max_rectangle, self.find(height))
        return max_rectangle

    def find(self, height):
        stack = []
        max_rectangle = 0
        for index, heights in enumerate(height + [0]):
            while stack and heights < height[stack[-1]]:
                pop_index = stack.pop()
                if stack:
                    left_bound = stack[-1]
                else:
                    left_bound = -1
                width = index - left_bound - 1
                max_rectangle = max(max_rectangle, width * height[pop_index])
            stack.append(index)
        return max_rectangle
'''
还是用单调栈
我们把每一行看成单独的rectangle problem 
遍历每一行 我们用height 去记录每一行的高度 如果遇到1的话 说明这是有效高度 那么这个index的高度➕1（因为要累加上一行的）
如果遇到0 那这个index的高度就变成0 
遍历完一行以后 我们用单调栈 去寻找每个rectangle所构成的最大值
然后返回
'''