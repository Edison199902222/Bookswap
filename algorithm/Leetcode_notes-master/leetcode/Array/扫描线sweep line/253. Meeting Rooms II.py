class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 首先这题是返回的是overlap 最多的那个区间 overlap 了几个
        # 其次，因为当前区间有可能不仅跟前一个overlap，也可能跟前前一个 overlap了
        # 或者有可能跟前一个overlap，但不跟前前一个overlap，也就是前前一个使用完 刚好当前区间可以使用
        # 所以不能单纯的sort，把interval 拆成两部分，start 跟 end 一起看
        points = []
        for i in intervals:
            points.append((i[0], 1))
            points.append((i[1], -1))
        points.sort()
        max_meeting = 0
        open_meeting = 0
        for i in points:
            open_meeting += i[1]
            max_meeting = max(max_meeting, open_meeting)
        return max_meeting


'''
扫描线算法
事情往往以区间来存在
区间的两端代表事情的开始和结束
就是遇到任何interval，将interval的start当成key存入，value+1，遇到end，存入。但是要-1；
用一个TreeMap存储，保证key的值是sort的
时间复杂度是O(N)
该方法可以用于如何calendar以及meeting room的题解。
'''