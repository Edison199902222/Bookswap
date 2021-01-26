
'''
类似于多路归并 + 扫描线， 因为对于每个end 来说，想要找到最接近的start，必须把start 全部都看了
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        end = []
        n = len(intervals)
        result = [-1] * n
        for i in range(n):
            # 记住， 往heap中放东西的时候需要放 tuple
            heapq.heappush(start, (-intervals[i][0], i))
            heapq.heappush(end, (-intervals[i][1], i))
        for i in range(n):
            end_value, index = heapq.heappop(end)
            if - start[0][0] >= - end_value:
                while start and -start[0][0] >= - end_value:
                    # 找到差值最小的那个 start value
                    start_value, start_index = heapq.heappop(start)
                # 注意index 是end value 的index， 我们是对每一个end value 找匹配差值最小的start value
                result[index] = start_index
                # 要把start value 重新放进去， 因为有可能之后的start value 都小于之后的 end value，但是这个start value肯定大于之后的end value
                # 因为 这之后的end value 都比当前的end value 小
                heapq.heappush(start, (start_value, start_index))
        return result


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        result = [-1 for i in range(n)]
        # 按照start 来排序，里面是（index,(start, end)）
        # 这样就可以使用二分，对于每个end 找到右边并且最接近的start就行了
        check_list = sorted([(index, x) for index, x in enumerate(intervals)], key=lambda x: x[1][0])
        for i in range(n):
            value = intervals[i][1]
            index = self.binary_search(check_list, value)
            if index != n:
                result[i] = check_list[index][0]
        return result

    def binary_search(self, arr, value):
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid][1][0] <= value:
                left = mid
            else:
                right = mid
        if arr[left][1][0] >= value:
            return left
        elif arr[right][1][0] >= value:
            return right
        return len(arr)