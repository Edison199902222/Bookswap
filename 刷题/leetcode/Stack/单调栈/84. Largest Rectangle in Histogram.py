class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = heights + [0]  # 因为如果是全递增的高度的话， 我们需要一个0 来更新
        stack = []
        result = 0  # 一定要初始化为0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                target_index = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = i - left - 1  # i 是右边界
                result = max(result, width * heights[target_index])
            stack.append(i)
        return result


'''
单调栈的问题
对于每个柱子而言 我们只需要找到 左边第一个比它小的 跟右边第一个比它小的 就是它的最大宽度
我们维持一个只递增的栈 里面储存的是每个点的index 
我们目的是 计算出以每个矩形的高度为高度 ✖ 上它的宽度 然后一个个进行比较
所以我们要找到 每个矩形 的左边界 跟右边界 去确定 每个矩形的宽度

stack 里面 因为是一个递增的数组 每个数的左边都比自己小 所以每个数的左边的数都是自己的左边界
那么我们只需要确定右边界
我们每一次 遇到一个矩阵 先判断它的高度是不是比我们stack中的peek 小
如果小的话 那么我们就能知道 这个矩阵的高度比前一个矩阵小 说明这是前一个矩阵的右边界
那么我们把stack 中 最后一个矩阵pop 出来 然后左边界是此时 stack中的 peek（也就是最后一个矩阵）
右边界就是我们当前的矩阵 然后用右边界 减去左边界 再减去1 就是stack pop 出来的矩阵的宽度
此时我们更新result 
然后再把当前矩阵 index 放进stack之中

'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # 扫两次
        # 往右边看最远可以到哪里
        # 往左边看最远可以到哪里
        left = self.find_left(heights)
        right = self.find_right(heights)
        result = 0
        for i in range(len(heights)):
            result = max(result, (right[i] - left[i] + 1) * heights[i])
        return result

    def find_right(self, heights):
        n = len(heights)
        result = [0 for i in range(n)]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                result[stack.pop()] = i - 1
            stack.append(i)
        # 防止全部相等的情况，比如【1，1，1】
        while stack:
            result[stack.pop()] = n - 1
        return result

    def find_left(self, heights):
        n = len(heights)
        result = [0 for i in range(n)]
        stack = []
        for i in range(n - 1, - 1, - 1):
            while stack and heights[i] < heights[stack[-1]]:
                result[stack.pop()] = i + 1
            stack.append(i)
        # 防止全部相等的情况，比如【1，1，1】
        while stack:
            result[stack.pop()] = 0
        return result