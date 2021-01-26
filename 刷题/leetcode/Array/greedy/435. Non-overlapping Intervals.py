class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 0
        end = float("-inf")
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end:
                end = i[1]
            else:
                result += 1
        return result
'''
按照 end 顺序 排序
用 end 去track 之前 合法的end 值
初始化 end 最小值
然后遍历数组
如果发现 现在的start 比之前 end 要小的话， result + 1 说明我们要剔除这个
不然的话 说明这个区间可以保存，end 更新
'''