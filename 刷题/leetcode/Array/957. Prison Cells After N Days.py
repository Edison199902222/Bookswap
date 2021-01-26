class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        check = set()
        flag = False
        j = 0
        # 算出以多少为一个轮回，
        while j < N:
            # 算出下一天的
            temp = self.next_day(cells)
            # 如果发现check中重复了，说明规律已经找到
            if str(temp) in check:
                flag = True
                break
            # 把下一天结果放进check中
            check.add(str(temp))
            j += 1
            # 重复的那一天不能算
            cells = temp

        if flag:
            N = N % len(check)
            for i in range(N):
                cells = self.next_day(cells)
        return cells

    def next_day(self, cells):
        temp = [0] * 8
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                temp[i] = 1
            else:
                temp[i] = 0
        return temp