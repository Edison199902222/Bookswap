'''
想法：我们首先要找到 要插入的起点到底是什么
因为这是按照第一个数字 的顺序排好的
所以 如果这个internval 的end 都小于我们的start 说明我们跟这个interval 无交集
找到了之后 并且要检查 是不是这个index 是不是等于我们的length 因为有可能 这个interval 永远跟我们的插入的没关系
找到了从哪里开始有关系了之后 我们的start 要取 跟 这个interval start点的最小值
然后我们找 end
如果我们的end 大于 interval的start的话 说明我们就有关系 再取 我们interval 跟 有关系interval end的最大值

'''


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        new_start = newInterval[0]
        new_end = newInterval[1]
        index = 0
        result = []
        # 找到start 的插入点
        # 遍历区间，如果发现start 比当前遍历的end 还要大的话，continue
        # 要插入的start 如果等于 当前区间的end 的话，也要合并
        # 要合并的区间是 有交集的区间！
        while index < n and new_start > intervals[index][1]:
            result.append(intervals[index])
            index += 1
        if index == n:
            result.append(newInterval)
            return result
        # 找到起始点
        new_start = min(intervals[index][0], new_start)
        # 找到起始点之后，开始找尾巴
        # 找到一个start 是大于当前end的，同时要更新end
        # 找到最后一个没有交集的区间，之前一直更新
        while index < n and new_end >= intervals[index][0]:
            new_end = max(new_end, intervals[index][1])
            index += 1
        result.append([new_start, new_end])
        while index < n:
            result.append(intervals[index])
            index += 1
        return result


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        result = []
        new_start, new_end = newInterval
        flag = False
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if not result:
                result.append(intervals[i])
            elif start <= result[-1][1]:
                start2, end2 = result.pop()
                result.append([min(start, start2), max(end, end2)])
            else:
                result.append(intervals[i])
            if new_start <= result[-1][1] and new_end >= result[-1][0]:
                flag = True
                start2, end2 = result.pop()
                result.append([min(new_start, start2), max(new_end, end2)])
        if not flag:
            result.append(newInterval)
        result = sorted(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1,3],[6,9]],[2,5]))