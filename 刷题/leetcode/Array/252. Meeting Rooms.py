class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)):
            if i == 0:
                continue
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


'''
按照 开始时间进行排序 
然后比较 每一个会议的开始时间 是不是在之前会议的结束时间 之后进行
那么就要看前一个会议结束的时候，下一个会议有没有开始。

'''
