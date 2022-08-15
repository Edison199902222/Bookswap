'''
在N个数组中找到第K大元素
'''
import heapq
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if not arrays:
            return None
        minheap = []
        count = 0
        for array in arrays:
            for elem in array:
                if count < k:
                    heapq.heappush(minheap, elem)
                    count += 1
                else:
                    heapq.heappushpop(minheap, elem)
        return heapq.heappop(minheap)
'''
维持 长度为k的 最小堆
我们每一次把元素放进去
然后因为是最小堆 会把 最小的元素pop出来 
所以 遍历完之后 整个堆就是 最 k 大的 元素都在heap中
然后遍历完 第k个大的元素就是顶部元素
'''