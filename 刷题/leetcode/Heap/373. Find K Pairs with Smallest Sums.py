class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k:
            return []
        heap = []
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(min(n1, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        result = []
        while len(result) < min(k, n1 * n2):
            sums, number1, number2, index = heapq.heappop(heap)
            result.append([number1, number2])
            if index + 1 < n2:
                heapq.heappush(heap, (number1 + nums2[index + 1], number1, nums2[index + 1], index + 1))
        return result


'''
使用最小堆 多路归并！！
我们先将 nums2 中最小的值 作为 配对 和 nums1 前k个元素进行组合 （如果没有前k个元素 就和 nums1中所有元素匹配）
然后 heapify 一下
然后 每次 从 heap中 pop 出一个来
把最小的 放进result中
并且 我们同时 移动 nums2 的指针 指向下一个 添加进heap之中
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
'''