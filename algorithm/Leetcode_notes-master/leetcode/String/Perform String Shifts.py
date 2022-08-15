class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        shifts = float("-inf")
        total_times = 0
        for i in range(len(shift)):
            direction = shift[i][0]
            times = shift[i][1]
            if i == 0:
                shifts = direction
                total_times = times
            elif shifts != direction:
                if times >= total_times:
                    shifts = direction

                    total_times = times - total_times
                else:
                    total_times -= times
            else:
                total_times += times
        total_times = total_times % len(s)

        if shifts == 0:
            s = s[total_times:] + s[:total_times]
        else:
            s = s[len(s) - total_times:] + s[:len(s) - total_times]
        return s
'''
利用抵消的原理
先算出 最终结果需要往哪里shift 并且shift几次

'''