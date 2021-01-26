'''
想法：
 sorted(intervals,key = lambda x:x[0]) 这是把一个list【list】 按照list【i】【0】的顺序排序
 排序之后
 如果第i个list 的start 比上一个的end 大的话 说明interval没有交集
 不然的话 就比较上一个的end 还是i的end 大
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals:return []
        ans = []
        for i in sorted(intervals,key = lambda x:x[0]):
            if not ans or i[0] > ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1],i[1])
        return ans