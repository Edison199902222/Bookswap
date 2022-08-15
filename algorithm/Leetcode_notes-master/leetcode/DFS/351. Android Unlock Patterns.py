class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 找出所有 解锁需要跨过的digit
        # 一共就八种
        self.dic = {(1, 3): 2, (1, 7): 4, (3, 9): 6, (7, 9): 8, (4, 6): 5, (2, 8): 5, (1, 9): 5, (3, 7): 5}
        self.count = 0
        # 对于键盘上每个数字，作为起始点，走一遍
        for i in range(1, 10):
            used = set()
            used.add(i)
            self.dfs(used, i, m, n)
        return self.count

    def dfs(self, used, cur_num, m, n):
        # 如果大于等于m的话，count 加1
        if len(used) >= m:
            self.count += 1
        if len(used) == n:
            return
        for i in range(1, 10):
            # 如果当前的下一个要选择的数字已经被used了，或者 下一个要走的数字 中间需要 数字，但这个数字没有在之前走过，那么是不合法
            if i in used or ((min(cur_num, i), max(cur_num, i)) in self.dic and self.dic[
                (min(cur_num, i), max(cur_num, i))] not in used):
                continue
            used.add(i)
            self.dfs(used, i, m, n)
            used.remove(i)
        return