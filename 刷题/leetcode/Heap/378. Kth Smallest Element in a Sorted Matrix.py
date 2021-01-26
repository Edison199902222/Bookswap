import heapq
'''
python 只有最小堆
然后整个heap 维持长度为k 大小的heap
其实就是 所有数字 取反后 越大自然变越小 越小的数字变越大
然后 因为是最小堆 最上面自然是最小的 并且我们设置 只有比root 大的话 才可以进入 比root大的意思是 取反之前 比root 小
那么 最后 这个heap中就有 最小的k个数字 
遍历完这个matrix 第一个自然就是第k个最小的数
heap 操作是 logn
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return -1
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                value = - matrix[row][col]
                if len(heap) < k:
                    heapq.heappush(heap,value)
                elif value > heap[0]:
                    heapq.heappushpop(heap,value)
        return -heap[0]
if __name__ =="__main__":
    solution = Solution()
    print(solution.kthSmallest([[1,2,3]],2))

'''
采用二分答案的方式来解决问题。 我们知道答案一定在[minNum,maxNum]这个区间内。 
对于某一个数res,我们将其与矩阵中的每一个数作对比，统计比他小于等于的数字的个数，如果个数正好等于k且res在矩阵中则答案为res。
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0] or not k:
            return None
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(matrix, mid) < k:
                left = mid
            else:
                right = mid
        if self.count(matrix, left) >= k:
            return left
        return right

    def count(self, matrix, value):
        count = 0
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= value:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count