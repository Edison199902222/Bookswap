class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        return result
'''
因为 a b 都是排序好的
我们 用两个指针， 一个指向A， 一个指向B
我们观察 区间交集的特点
发现 如果 a的start 比 b 的end 小， b 的start 比 a 的end 小的话
说明这两个 区间有交集 
那么 我们就 取start 的最大值 end的最小值 就是交集的部分
然后比较 下一个该移动哪一个指针
如果 a的end 小于等于 b的end的话
那么就移动a的指针，因为 b 的区间更长
反之 移动 b的指针
'''