class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """

        def day(y, m, d):
            # 先算出有几年是闰年， 闰年要加一天
            yd = 365 * (y - 1970)
            for i in range(1970, y):
                if i % 4 == 0:
                    yd += 1
            month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            md = sum(month[:m - 1])
            # 看月份，如果当前年是闰年的话，并且大于2的话，今年还需要加一天
            if y % 4 == 0 and y != 2100 and m > 2:
                md += 1
            return yd + md + d

        date1 = date1.split("-")
        date2 = date2.split("-")
        y1 = int(date1[0])
        m1 = int(date1[1])
        d1 = int(date1[2])

        y2 = int(date2[0])
        m2 = int(date2[1])
        d2 = int(date2[2])

        days1 = day(y1, m1, d1)
        days2 = day(y2, m2, d2)

        return abs(days1 - days2)

